import sys
import runpy
import snoop


def _format_path(path):
    return path[:-3].replace('/', '.')


@snoop
def run_script(py_script):
    runpy.run_module(_format_path(py_script), {}, "__main__")

run_script(sys.argv[1])
