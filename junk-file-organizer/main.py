#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

from organizeByYear import organize_by_year
from organizeBySize import organize_by_size
from organizeByExtension import organize_by_extension
from organizeByType import organize_by_type


def main():

    print("")
    print("*" * 75)
    print("*" + " " * 26 + " JUNK FILE ORGANIZER " + " " * 26 + "*")
    print("*" * 75)
    print("*" + " " * 73 + "*")
    print("*" + " " * 23 + " # For organizing files by " + " " * 23 + "*")
    print("*" + " " * 73 + "*")
    print("*" + " " * 5 + "size      : " + " python3 -o size -p <path>" +
          " " * 30 + "*")
    print("*" + " " * 5 + "year      : " + " python3 -o year -p <path>" +
          " " * 30 + "*")
    print("*" + " " * 5 + "type      : " + " python3 -o type -p <path>" +
          " " * 30 + "*")
    print("*" + " " * 5 + "extension : " + " python3 -o extension -p <path>" +
          " " * 25 + "*")
    print("*" + " " * 73 + "*")
    print("*" + " " * 29 + " #  Flags used " + " " * 29 + "*")
    print("*" + " " * 73 + "*")
    print("*" + " " * 5 + "-p / --path  : " + " absolute path " + " " * 38 +
          "*")
    print("*" + " " * 5 + "-o / --order : " + " order by " + " " * 43 + "*")
    print("*" + " " * 5 + "-h / --help  : " + " for help " + " " * 43 + "*")
    print("*" + " " * 73 + "*")
    print("*" + " " * 73 + "*")
    print("*" + " " * 5 +
          "-p/--path <path>  &  -o/--order <order>  are mandatory " +
          " " * 13 + "*")
    print("*" + " " * 73 + "*")
    print("*" * 75)

    parser = argparse.ArgumentParser()

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
        choices=['extension', 'size', 'year', 'type'],
    )

    args = parser.parse_args()

    path = args.path
    organizeBy = args.order

    if organizeBy == 'extension':
        organize_by_extension(path)
    elif organizeBy == 'size':
        organize_by_size(path)
    elif organizeBy == 'year':
        organize_by_year(path)
    elif organizeBy == 'type':
        organize_by_type(path)
    else:
        print('Wrong Choice for Organizing')


if __name__ == '__main__':
    main()
