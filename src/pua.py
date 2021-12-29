import os
import runpy
import sys

from src.core import translate_file

def commandline():
    """run pua file in CLI

    >>> pua file.pua 
    """

    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("pua-lang: file '%s' does not exists" % file_path)
        sys.exit(1)
    
    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))
    sources = translate_file(file_path)
    runpy._run_module_code(sources, mod_name="__main__")


if __name__=="__main__":
    commandline()