#!/usr/bin/python3

# Name: Sectoday
# Version: 1.1.0
# Description: This is a program that converts seconds to days.
# Author: LeonardoM011
# Date: 10/14/2018

import argparse

program_description = \
    "This is a program that converts seconds to days."
program_version = "%(prog)s 1.1.0"


def main():
    parser = argparse.ArgumentParser(description=program_description)

    seconds_help = "Type in a number of seconds."
    parser.add_argument(
        'seconds', type=int, nargs=1, help=seconds_help)

    parser.add_argument(
        '-v', '--version', action='version', version=program_version)

    args = parser.parse_args()

    seconds = args.seconds[0]

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    print("{} days, {} hours, {} minutes and {} seconds".format(
        days, hours, minutes, seconds))


if __name__ == '__main__':
    main()
