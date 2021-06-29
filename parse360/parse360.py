#!/usr/bin/python

import sys


def checkarg(argv):
    # check if args exist
    if len(argv) == 0:
        raise Exception("Please pass in a video to transcode")
    # check for file or folder
    for arg in argv:
        if (not check360file(arg)):
            raise TypeError("Wrong file type, gopro .360 file only")


def check360file(file):
    return file.endswith(".360")


def main(argv):
    checkarg(argv)
    print(".360 file found")


if __name__ == "__main__":
    main(sys.argv[1:])
