#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Gashly Crumb
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashly Crumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs = '+',
                        help='Letter to find line for')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default= 'gashlycrumb.txt')


    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()

    phrases = {}
    for line in args.file:
        first = line[0]
        phrases[first] = line.strip()

    for letter in args.letter:
        if letter.upper() in phrases:
            print(phrases[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
