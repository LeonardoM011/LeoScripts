#!/usr/bin/python3

# Name: lreplace
# Version: 1.0.0
# Description: Replaces file name that begins with a number with a string.
# Author: LeonardoM011
# Date: 1/9/2019

import os
import argparse

program_description = \
    "Replaces file name that begin with number with some text."
program_version = "%(prog)s 1.0.0"


def replace_numbers(name, replace_with, incl_period):
    while True:
        if name[0].isdigit() \
                or (incl_period is True and name[0] == '.'):
            name = name[1:]
            continue
        break
    name = replace_with + name
    return name


def main():
    parser = argparse.ArgumentParser(description=program_description)

    path_help = "Path to folder for files to rename."
    parser.add_argument(
            'path', type=str, nargs=1, help=path_help)

    text_help = "Text that replaces numbers."
    parser.add_argument(
            'text', type=str, nargs=1, help=text_help)

    period_help = "Weather or not to replace period too."
    parser.add_argument(
            '-s', '--include-period', action='store_true', help=period_help)

    parser.add_argument(
            '-v', '--version', action='version', version=program_version)

    args = parser.parse_args()

    for filename in os.listdir(args.path[0]):
        if filename[0].isdigit():
            newname = replace_numbers(
                    filename, args.text[0], args.include_period[0])
            filename = args.path[0] + '/' + filename
            newname = args.path[0] + '/' + newname
            os.rename(filename, newname)


if __name__ == '__main__':
    main()
