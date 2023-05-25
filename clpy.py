#!/usr/bin/env python
from sys import argv, exit, stdin, stderr
from os import path, isatty
from typing import Tuple

VERSION = "unknown"

def die(*args, **kwargs):
    print(*args, **kwargs, file=stderr)
    exit(1)


def readFile(file: str) -> str:
    if not path.exists(file):
        die("No such file or directory:", file)
    if not path.isfile(file):
        die("Not a regular file:", file)
    with open(file, "r", encoding="utf8") as f:
        return f.read()[0:-1]


def parseArgs() -> Tuple[str, str]:
    if len(argv) < 2 or len(argv) > 3 or "-h" in argv or "--help" in argv:
        die("Uage:", path.basename(argv[0]), "CMD [FILE]")
    if "-v" in argv or "--version" in argv:
        die(VERSION)

    cmd = argv[1]
    if len(argv) == 3:
        inp = readFile(argv[2])
    elif isatty(0):
        inp = ""
    else:
        inp = stdin.read()
    return cmd, inp


imp = __import__


def main():
    cmd, inp = parseArgs()
    try:
        print(eval(cmd, {"inp": inp, "imp": imp}))
    except Exception as e:
        die(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        die(path.basename(argv[0]), "encountered an unexpected error: ", e)
