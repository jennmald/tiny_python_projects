#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Crow's nest: working with strings
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ """

    args = get_args()
    word_arg = args.word
    first = word_arg[0].lower()
    vowels = ['a','e', 'i', 'o', 'u']
    if first in vowels:
        print('Ahoy, Captain, an '+ word_arg +' off the larboard bow!')
    else:
        print('Ahoy, Captain, a '+ word_arg +' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
