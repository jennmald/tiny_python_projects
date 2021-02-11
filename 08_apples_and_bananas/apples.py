#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Apples and Bananas
"""

import argparse
import os 

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Text to replace vowels')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace',
                        metavar='str',
                        type=str,
                        default='a',
                        choices = list('aeiou'))
    args = parser.parse_args()

    # optional file name
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip() 

    return args


# --------------------------------------------------
def main():
    lower_vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    args = get_args()
    txt = args.text
    to_vowel = args.vowel
    new_txt = ''
    for char in txt:
        if char in lower_vowels:
            new_txt= new_txt + to_vowel.lower()
        elif char in upper_vowels:
            new_txt = new_txt + to_vowel.upper()
        else: 
            new_txt = new_txt + char
    print(new_txt)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
