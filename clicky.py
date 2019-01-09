#!/usr/bin/python3

# Name: Clicky
# Version: 1.1.0
# Description: This is a program that automatically presses left click.
# Author: LeonardoM011
# Date: 10/14/2018

import time
import argparse
from pymouse import PyMouse

program_description = \
    "This is a program that automatically presses left click."
program_version = "%(prog)s 1.1.0"

my_mouse = PyMouse()


def pressy():
    x, y = my_mouse.position()
    # 1 is left click
    my_mouse.click(x, y, 1)


def main():
    parser = argparse.ArgumentParser(description=program_description)

    parser.add_argument(
        '-v', '--version', action='version', version=program_version)

    status = input("Start? [Y/n] ")
    if status == 'y' or status == 'Y':
        while True:
            pressy()
            time.sleep(1)


if __name__ == "__main__":
    main()
