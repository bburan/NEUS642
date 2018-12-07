import importlib
import os
import sys


def print_report():
    if (sys.version_info.major == 3) and (sys.version_info.minor == 6):
        print(f'Correct version of Python is installed. You are running {sys.version_info.major}.{sys.version_info.minor}.')
    else:
        print(f'Wrong version of Python is installed. You are running {sys.version_info.major}.{sys.version_info.minor}.')
        return

    environment = os.environ['CONDA_DEFAULT_ENV']
    error = False

    if environment != 'NEUS642_final':
        print(f'Your environment is "{environment}" but you should be using "NEUS642_final"')
        return

    for module in ('numpy', 'scipy', 'palettable'):
        try:
            importlib.import_module(module)
            print(f'You successfully installed {module}')
        except:
            print(f'{module} is missing')
            error = True

    if not error:
        print('Congratulations, you successfully set up your environment.')
