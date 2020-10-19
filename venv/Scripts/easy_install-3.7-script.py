<<<<<<< HEAD
#!E:\pycharm\PSI2020\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install-3.7'
__requires__ = 'setuptools==39.1.0'
=======
#!C:\Users\Mateusz\PycharmProjects\PSI2020\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install-3.7'
__requires__ = 'setuptools==40.8.0'
>>>>>>> ba1fec0d9de15e24108763b44a9da4004867f46a
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
<<<<<<< HEAD
        load_entry_point('setuptools==39.1.0', 'console_scripts', 'easy_install-3.7')()
=======
        load_entry_point('setuptools==40.8.0', 'console_scripts', 'easy_install-3.7')()
>>>>>>> ba1fec0d9de15e24108763b44a9da4004867f46a
    )
