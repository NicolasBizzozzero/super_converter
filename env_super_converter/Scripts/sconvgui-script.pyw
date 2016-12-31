#!W:\projects\Super-Converter\env_super_converter\Scripts\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Super-Converter==0.1.0','gui_scripts','sconvgui'
__requires__ = 'Super-Converter==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Super-Converter==0.1.0', 'gui_scripts', 'sconvgui')()
    )
