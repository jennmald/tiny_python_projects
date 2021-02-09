#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/9/2021
Purpose: Make all text uppercase
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler- Create upper case output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # maybe a text arguement or a file name
    parser.add_argument('text',
                        metavar='str',
                        type = str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type = str,
                        help='Output filename',
                        default ='')

    args = parser.parse_args()
    # check if text is name of file
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args 


# --------------------------------------------------
def main():
    """ Upper-case inputs in std output or a file """
    args = get_args()
    if args.outfile:
        file_out = open(args.outfile, 'wt')
        file_out.write(args.text.upper() + '\n')
    else:
        print(args.text.upper())    


# --------------------------------------------------
if __name__ == '__main__':
    main()
