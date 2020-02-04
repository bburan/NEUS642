import numpy as np

def scale_torcs(TorcValues,Params):
    ScaledTorcs = dict()
    for key,value in TorcValues.items():
        [xsiz, tsiz] = value.shape
        temp = value
        if Params['xSize'] != xsiz & Params['tSize'] != tsiz:
            temp1 = interpft(interpft(temp, Params['xSize'], 0), Params['tSize'], 1)

            scl = np.max(np.abs([np.min(np.min(temp1)), np.max(np.max(temp1))]))

            temp2 = temp*Params['mod_depth']/scl
        ScaledTorcs[key] = temp2
    return ScaledTorcs

def insteadofbin(resp,binsize,mf=1):
    '''
    Downsample spike histogram from resp (resolution mf) to resolution by binsize(ms)
    :param resp: response data (comes from spikeperiod
    :param binsize: calculated size of bins (basep/stimtime = binsize)
    :param mf: multiplication factor, default 1
    :return: returns downsampled spike histogram
    '''

    if len(resp.shape) >= 2:
        [spikes,records] = resp.shape
    else:
        resp = np.expand_dims(resp, axis=1)
        [spikes,records] = resp.shape

    outlen = int(spikes / binsize / mf)

    if outlen - np.floor(outlen/1) * 1 > 1:
        print('Non-integer # bins. Result may be distorted')

    outlen = np.round(outlen)
    dsum = np.zeros([outlen,records])

    for rec in range(records):
        temprec = np.fft.fft(resp[:,rec])             #fft for each

        if outlen % 2 == 0:                           #if even length, create middle point
            temprec[np.ceil((outlen-1)/2)+1] = np.abs(temprec[np.ceil(outlen-1)/2]+1)

        dsum[:, rec] = np.fft.ifft(np.concatenate((temprec[0:int(np.ceil((outlen - 1) / 2) + 1)], np.conj(
            np.flipud(temprec[1:int(np.floor((outlen - 1) / 2) + 1)]))))).real

    return dsum

def makepsth(dsum,fhist,startime,endtime,mf=1):
    '''
    Creates a period histogram according to period implied by input freq fhist
    :param dsum: spike data
    :param fhist: the frequency for which the histogram is performed
    :param startime: the start of the histogram data (ms)
    :param endtime: the end of the histogram data (ms)
    :param mf: multiplication factor
    :return: psth
    '''
    if fhist == 0:
        fhist = 1000/(endtime-startime)
    dsum = dsum[:]

    period = int(1000 * (1/fhist) * mf)
    startime = startime * mf
    endtime = endtime * mf

    if endtime > len(dsum):
        endtime = len(dsum)

    fillmax = int(np.ceil(endtime/period) * period)
    if fillmax > endtime:
        dsum[endtime+1:fillmax] = np.nan
        endtime = fillmax

    dsum[:startime] = np.nan
    repcount = int(fillmax / period)
    dsum = np.reshape(dsum[:endtime],(period,repcount),order='F')

    wrapdata = np.nansum(dsum,1)
    cnorm =  np.sum(np.logical_not(np.isnan(dsum)),1)

    return wrapdata,cnorm


def response_compiler(stacked,Params):
    '''
    Create from response data a single vector of average responses to torcs
    :param stacked: raster data
    :param Params: some parameters
    :return: a 1D of responses
    '''
    FirstStimTime = Params['basep']
    RespCat = dict()
    for rep in range(stacked.shape[1]):
        for rec in range(stacked.shape[2]):

            spkdata = stacked[:,rep,rec]

            [Dsum,cnorm] = makepsth(spkdata.copy(), int(1000 / Params['basep']), int(FirstStimTime), Params['stdur'], Params['mf'])

            #Time to normalize by #cycles. May be variable for TORCs, since they could be shorter than length in exptparams
            Dsum = Dsum / (cnorm + (cnorm == 0))

            if Params['binsize'] > 1/Params['mf']:
                Dsum = insteadofbin(Dsum, Params['binsize'], Params['mf'])
            Dsum = Dsum * (1000/Params['binsize'])                                           #normalization by bin size

            if rec == 0:
                respcatval = Dsum
            else:
                respcatval = np.concatenate((respcatval,Dsum),axis=None)

        RespCat[rep] = respcatval

    avgResp = np.mean(np.array(list(RespCat.values())),axis=0)

    return avgResp


def interpft(x,ny,dim=0):
    '''
    Function to interpolate using FT method, based on matlab interpft()
    :param x: array for interpolation
    :param ny: length of returned vector post-interpolation
    :param dim: performs interpolation along dimension DIM, default 0
    :return: interpolated data
    '''

    if dim >= 1:                                         #if interpolating along columns, dim = 1
        x = np.swapaxes(x,0,dim)                         #temporarily swap axes so calculations are universal regardless of dim
    if len(x.shape) == 1:                                #interpolation should always happen along same axis ultimately
        x = np.expand_dims(x,axis=1)

    siz = x.shape
    [m, n] = x.shape

    a = np.fft.fft(x,m,0)
    nyqst = int(np.ceil((m+1)/2))
    b = np.concatenate((a[0:nyqst,:], np.zeros(shape=(ny-m,n)), a[nyqst:m, :]),0)

    if np.remainder(m,2)==0:
        b[nyqst,:] = b[nyqst,:]/2
        b[nyqst+ny-m,:] = b[nyqst,:]

    y = np.fft.irfft(b,b.shape[0],0)
    y = y * ny / m
    y = np.reshape(y, [y.shape[0],siz[1]])
    y = np.squeeze(y)

    if dim >= 1:                                        #switches dimensions back here to get desired form
        y = np.swapaxes(y,0,dim)

    return y

def torcmaker(TORC,Params):
    '''
    Returns the TORC - option to plot each torc commented out
    This is a fairly core calculation
    :param TORC: TORC data from torc dictionary
    :param Params: TorcObject containing info about the torc
    :return: the torc itself
    '''
    lfreq = TORC['LowestFrequency']
    hfreq = TORC['HighestFrequency']
    Scales = TORC['Scales']
    Amplitude = TORC['RippleAmplitude']
    Phase = TORC['Phase']
    Rate = TORC['Rates']

    octaves = np.log2(hfreq)-np.log2(lfreq)
    normed_scales = [s*octaves for s in Scales]
    cycles_per_sec = 1000/Params['T']
    normed_tempmod= [t/cycles_per_sec for t in Rate]
    numcomp = Params['numcomp']
    leng = Params['leng']

    # somehow we've figured out that final spectrogram should be
    # (numcomp spectral dimension rows) X (leng time samples per TORC cycle)

    stimHolder = np.zeros((numcomp,leng),dtype=complex)
    c = [np.floor(numcomp/2), np.floor(leng/2)]

    for i, (vel,phs,amp,scl) in enumerate(zip(normed_tempmod,Phase,Amplitude,normed_scales)):
        # figure out index in fourier domain for each ripple
        v1=int(vel+c[1])
        v2=int(c[1]-vel)
        s1=int(scl+c[0])
        s2=int(c[0]-scl)

        stimHolder[s1,v1] = (amp/2)*np.exp(1j*(phs-90)*np.pi/180)
        stimHolder[s2,v2] = (amp/2)*np.exp(-1j*(phs-90)*np.pi/180)

    y_sum = (np.fft.ifft2(np.fft.ifftshift(stimHolder*(leng*numcomp)))).real
    return y_sum

def best_frequency(strf,Params):
    strfsmooth = interpft(strf, 100, 0)
    ff = np.exp(np.linspace(np.log(Params['lfreq']), np.log(Params['hfreq']), strfsmooth.shape[0]))
    mm = np.mean(strfsmooth[:,:7] * (1 * (strfsmooth[:,:7] > 0)), 1)
    bfidx = int(sum(((mm == np.max(mm)).ravel().nonzero())))
    bf = np.round(ff[bfidx])
    return bf
