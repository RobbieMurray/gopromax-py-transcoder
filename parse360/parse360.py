#!/usr/bin/python

import argparse
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def checkarg(args):
    if args.file:
        if (not check360file(args.file)):
            raise TypeError('Wrong file type, gopro .360 file only')
        else:
            print(args.file + ' - .360 file found')
            # TODO continue processing
    if args.path:
        print(args.path)
        for *_, files in os.walk(args.path):
            # TODO Support Multiple directories?
            count = 0
            for file in files:
                if not file.startswith('.') and check360file(file):
                    count += 1
                    print(file + ' - .360 file found')
            print(str(count) + ' .360 files found')
            # TODO continue processing


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
