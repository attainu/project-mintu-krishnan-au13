#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

from organizeByDate import organize_by_date
from organizeBySize import organize_by_size
from organizeByExtension import organize_by_extension
from organizeByType import organize_by_type


def main():

    parser = \
        argparse.ArgumentParser(description='''
    -------------------------------
    -----------------------------------------------
    . . . . . . . . . . . .
    Welcome to Junk File Organizer
    . . . . . . . . . . . .
    --------------------------------
    ----------------------------------------------
    ''')

    parser.add_argument(
        '-p',
        '--path',
        metavar='',
        required=True,
        help='{path} - path of the directory to organize ')  # default='.',

    parser.add_argument(
        '-o',
        '--order',
        default='type',
        help='{extension,size,date,type} - the way you need to organize',
        metavar='',
        choices=['extension', 'size', 'date', 'type'],
    )

    args = parser.parse_args()

    path = args.path
    organizeBy = args.order

    if organizeBy == 'extension':
        organize_by_extension(path)
    elif organizeBy == 'size':
        organize_by_size(path)
    elif organizeBy == 'date':
        organize_by_date(path)
    elif organizeBy == 'type':
        organize_by_type(path)
    else:
        print('Wrong Choice for Organizing')


if __name__ == '__main__':
    main()
