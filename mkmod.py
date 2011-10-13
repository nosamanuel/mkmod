import os
import sys

__version__ = '0.1'

INIT_PY = '__init__.py'


def touch(path):
    with file(path, 'a'):
        os.utime(path, None)


def mkmod(path):
    # Replace dots with system paths and strip separators
    path = os.path.join(*path.strip(os.path.sep).split('.')) or '.'

    # Create entire directory structure
    if not os.path.exists(path):
        os.makedirs(path)

    # Ensure init.py exists at each level
    while path:
        touch(os.path.join(path, INIT_PY))
        path, remainder = os.path.split(path)


def mkmod_main(script, path='.', **args):
    mkmod(path)


def main():
    mkmod_main(*sys.argv)
