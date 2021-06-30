#!/usr/bin/python

import argparse
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def checkarg(args):
    # check for file or folder
    if args.file:
        if (not check360file(args.file)):
            raise TypeError('Wrong file type, gopro .360 file only')
        else:
            print('.360 file found')
    if args.path:
        # TODO Loop through directory and check each file
        print(args.path)


def check360file(file):
    # TODO check for relevant meta-data in file
    return file.endswith('.360')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='the file that you wish to transcode', type=str)
    parser.add_argument(
        '-p', '--path', help='directory to bulk parse', type=dir_path)
    args = parser.parse_args()
    if not (args.file or args.path):
        parser.error('No action requested, add --file or --path')
    checkarg(args)


if __name__ == '__main__':
    main()
