The exercise for this week requires a few additional packages installed to the `NEUS642` environment. To install these, open an Anaconda prompt and run the following:

	conda activate NEUS642
	conda install cython 'testpath<0.4'
	pip install czifile

How do you know you need to do these in this order? We know that we need to install czifile for the exercise. I typically try `conda install` first to see what happens:

	conda install czifile

However, I got this output:

	Solving environment: failed

	PackagesNotFoundError: The following packages are not available from current channels:

	  - czifile

	Current channels:

	  - https://repo.anaconda.com/pkgs/main/linux-64
	  - https://repo.anaconda.com/pkgs/main/noarch
	  - https://repo.anaconda.com/pkgs/free/linux-64
	  - https://repo.anaconda.com/pkgs/free/noarch
	  - https://repo.anaconda.com/pkgs/r/linux-64
	  - https://repo.anaconda.com/pkgs/r/noarch
	  - https://repo.anaconda.com/pkgs/pro/linux-64
	  - https://repo.anaconda.com/pkgs/pro/noarch

	To search for alternate channels that may provide the conda package you're
	looking for, navigate to

		https://anaconda.org

	and use the search bar at the top of the page.

Since a search on https://anaconda.org for `czifile` yielded no results, I checked to see if the package was available via `pip`. Pip is Python's main package manager and is an alterative to conda. Although `conda` has largely replaced `pip`, not all Python packages are available via conda. Fortunately, you can use both conda and pip to install packages into your environment. You should always prefer conda where possible (it's better about resolving dependencies). So, the next step I did was try to install via pip:

	pip install czifile

It didn't *quite* work as the following output shows:

	Collecting czifile
	  Using cached https://files.pythonhosted.org/packages/c2/27/770c8099c667590d96f769657465a6da8b3921ca433c5cd550680c1ae760/czifile-0.1.5.tar.gz
		Complete output from command python setup.py egg_info:
		Traceback (most recent call last):
		  File "<string>", line 1, in <module>
		  File "/tmp/pip-install-fmobe664/czifile/setup.py", line 7, in <module>
			from Cython.Distutils import build_ext
		ModuleNotFoundError: No module named 'Cython'
		
		----------------------------------------
	Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-fmobe664/czifile/

Ok, we're getting closer. We now know we need a module called `cython`. Let's see if conda has this available.

	conda install cython

Success! We get the following output:

	Solving environment: done

	## Package Plan ##

	  environment location: /home/bburan/bin/miniconda3/envs/NEUS642

	  added / updated specs: 
		- cython


	The following packages will be downloaded:

		package                    |            build
		---------------------------|-----------------
		cython-0.28.5              |   py37hf484d3e_0         3.3 MB

	The following NEW packages will be INSTALLED:

		cython: 0.28.5-py37hf484d3e_0

	Proceed ([y]/n)? 


	Downloading and Extracting Packages
	cython-0.28.5        | 3.3 MB    | ##################################### | 100% 
	Preparing transaction: done
	Verifying transaction: done
	Executing transaction: done

Great, now let's try to install `czifile` again via pip:

	pip install czifile

Still not working, as the following output shows. 

	Collecting czifile
	Collecting tifffile (from czifile)
	Requirement already satisfied: cython in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (0.28.5)
	Requirement already satisfied: scipy>=0.19.0 in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (1.1.0)
	Collecting lxml (from czifile)
	  Using cached https://files.pythonhosted.org/packages/7a/6b/a3d2d3c3075617edcbfc272d79281e812b1a94dab37923b1d06fdfe2e906/lxml-4.2.5-cp37-cp37m-manylinux1_x86_64.whl
	Requirement already satisfied: numpy>=1.8.2 in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (1.15.2)
	Exception:
	Traceback (most recent call last):
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2862, in _dep_map
		return self.__dep_map
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2669, in __getattr__
		raise AttributeError(attr)
	AttributeError: _DistInfoDistribution__dep_map

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py", line 93, in __init__
		req = REQUIREMENT.parseString(requirement_string)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1632, in parseString
		raise exc
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1622, in parseString
		loc, tokens = self._parse( instring, 0 )
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1379, in _parseNoCache
		loc,tokens = self.parseImpl( instring, preloc, doActions )
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 3395, in parseImpl
		loc, exprtokens = e._parse( instring, loc, doActions )
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1383, in _parseNoCache
		loc,tokens = self.parseImpl( instring, preloc, doActions )
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 3183, in parseImpl
		raise ParseException(instring, loc, self.errmsg, self)
	pip._vendor.pyparsing.ParseException: Expected stringEnd (at char 33), (line:1, col:34)

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2942, in __init__
		super(Requirement, self).__init__(requirement_string)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py", line 97, in __init__
		requirement_string[e.loc:e.loc + 8]))
	pip._vendor.packaging.requirements.InvalidRequirement: Invalid requirement, parse error at "'; extra '"

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_internal/basecommand.py", line 228, in main
		status = self.run(options, args)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_internal/commands/install.py", line 318, in run
		self._warn_about_conflicts(to_install)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_internal/commands/install.py", line 442, in _warn_about_conflicts
		package_set, _dep_info = check_install_conflicts(to_install)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_internal/operations/check.py", line 89, in check_install_conflicts
		state = create_package_set_from_installed()
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_internal/operations/check.py", line 39, in create_package_set_from_installed
		retval[name] = PackageDetails(dist.version, dist.requires())
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2613, in requires
		dm = self._dep_map
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2864, in _dep_map
		self.__dep_map = self._compute_dependencies()
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2874, in _compute_dependencies
		reqs.extend(parse_requirements(req))
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2935, in parse_requirements
		yield Requirement(line)
	  File "/home/bburan/bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages/pip/_vendor/pkg_resources/__init__.py", line 2944, in __init__
		raise RequirementParseError(str(e))
	pip._vendor.pkg_resources.RequirementParseError: Invalid requirement, parse error at "'; extra '"

You may not get this error as it is a bug in a particular version of a library that conda installed. I just happend to be unlucky in that I tried to install these libraries when a buggy version was available via the conda repository. 

This error message is what's known as a traceback. How do we figure out what to do? Well, let's try Googling for the error message at the bottom of the traceback:

	pip._vendor.pkg_resources.RequirementParseError: Invalid requirement, parse error at "'; extra '"

The first hit [takes us to Stackoverflow](https://stackoverflow.com/questions/52582563/pip-install-attributeerror-distinfodistribution-dep-map). Here, the answer tells us that there's a bug in a particular library, `testpath`, and that we need to downgrade:

	conda install 'testpath<0.4'

Why was this in our environment? It's a dependency of some other package we explicitly installed. After trying the command above, we can try installing czifile again:

	pip install czifile

Success! Yes, you do get a few warnings, but you can ignore those because the key message is `Successfully installed zcifile-0.1.5 lxml-4.2.5 tifffile-0.15.1` as shown in the output:

	Collecting czifile
	Requirement already satisfied: cython in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (0.28.5)
	Requirement already satisfied: numpy>=1.8.2 in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (1.15.2)
	Collecting lxml (from czifile)
	  Using cached https://files.pythonhosted.org/packages/7a/6b/a3d2d3c3075617edcbfc272d79281e812b1a94dab37923b1d06fdfe2e906/lxml-4.2.5-cp37-cp37m-manylinux1_x86_64.whl
	Collecting tifffile (from czifile)
	Requirement already satisfied: scipy>=0.19.0 in ./bin/miniconda3/envs/NEUS642/lib/python3.7/site-packages (from czifile) (1.1.0)
	twisted 18.7.0 requires PyHamcrest>=1.9.0, which is not installed.
	jupyter-console 5.2.0 has requirement prompt-toolkit<2.0.0,>=1.0.0, but you'll have prompt-toolkit 2.0.5 which is incompatible.
	Installing collected packages: lxml, tifffile, czifile
	Successfully installed czifile-0.1.5 lxml-4.2.5 tifffile-0.15.1

Ok, we also need a package called `PIL`. This is actually *very unintuitive*. You have to install pillow, not PIL. How do you know? This is one of the rare exceptions where the import name does not match the package name. You just have to Google it.
