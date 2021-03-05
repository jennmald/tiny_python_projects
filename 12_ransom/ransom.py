#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 3/5/2021
Purpose: Ransom
"""

import argparse
import os
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Ransom',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

def choose(char):
    if random.choice([0,1]):
        return char.upper()
    else:
        return char.lower()

def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'c'
    assert choose('d') == 'd'
    random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    ransom_text = ''
    for char in args.text:
        ransom_text+=choose(char)
    print(ransom_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
