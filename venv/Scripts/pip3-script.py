<<<<<<< HEAD
#!E:\pycharm\PSI2020\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==10.0.1','console_scripts','pip3'
__requires__ = 'pip==10.0.1'
=======
#!C:\Users\Mateusz\PycharmProjects\PSI2020\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.3','console_scripts','pip3'
__requires__ = 'pip==19.0.3'
>>>>>>> ba1fec0d9de15e24108763b44a9da4004867f46a
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
<<<<<<< HEAD
        load_entry_point('pip==10.0.1', 'console_scripts', 'pip3')()
=======
        load_entry_point('pip==19.0.3', 'console_scripts', 'pip3')()
>>>>>>> ba1fec0d9de15e24108763b44a9da4004867f46a
    )
