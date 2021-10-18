import sys

from .conv import build


def main_func():
    args = list(map(lambda x: print if x == "print" else x, sys.argv[1:]))

    build(*args)
