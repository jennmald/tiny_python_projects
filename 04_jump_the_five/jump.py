#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Decrypt numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text

    decrypt = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0',
               '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    output = ''
    for char in text_arg:
        if char in decrypt:
            output = output + decrypt[char]
        else:
            output = output+char
    print(output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
