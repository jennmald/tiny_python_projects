#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 4/13/2021
Purpose: Gematria: Numerical Encoding of text
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help = 'Input text or file')

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
       args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def numerical(word):
   return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))

# --------------------------------------------------
def test_numerical():
    # test numerical method
    assert numerical("a") == "97"
    assert numerical("abc") == "294"
    assert numerical("ab'c") == "294"
    assert numerical("4a-b'c,") == "346"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    for line in args.text.splitlines():
       print(' '.join(map(numerical, line.split())))

# --------------------------------------------------
if __name__ == '__main__':
    main()
