#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/9/2021
Purpose: Randomly reordering the middle of words
"""

import argparse
import os
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scrambler (scramble middle letters of words)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # maybe a text argument or a file name
    parser.add_argument('text',
                        metavar='str',
                        type = str,
                        help='Input string or file')

    # seed - defaults to none
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    # check if text is name of file
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args 


# --------------------------------------------------
def main():
    """ Split and scramble words in text using regular expression """
    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))


# --------------------------------------------------
def scramble(word):
    """ Scramble a word """
    scrambled = ''
    #determine correct length and character type
    if len(word)>=4 and re.match(r'\w+',word):
        #middle of the word
        middle = list(word[1:-1])
        random.shuffle(middle)
        #back to string
        mid_chars = ''
        for l in middle:
            mid_chars+=l
        scrambled = word[0] + scrambled + mid_chars + word[-1]
    else:
        scrambled = word
    return scrambled


# --------------------------------------------------
def test_scramble():
    """ Test Scramble """
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
