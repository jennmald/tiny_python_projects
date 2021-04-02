#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 4/2/2021
Purpose: Using regex to create rhyming words
"""

import argparse
import string as s
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rhymer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                         help = 'A word to rhyme',
                         metavar = 'word',
                         type = str,
                         default = '')

    return parser.parse_args()

#--------------------------------------------------
def stemmer(word):
    word = word.lower()
    vowels = 'aeiou'
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])
    match = re.match('([' + consonants + ']+)?' 
                    '([' + vowels + '])'
                    '(.*)', word)
    if match:
       p1 = match.group(1) or ''
       p2 = match.group(2) or ''
       p3 = match.group(3) or ''
       return (p1, p2+p3)
    else:
       return (word, '')

#---------------------------------------------------
def non_reggex_stemmer(word):
    word = word.lower()
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z', '1', '2', '3', '4', '5', '6', '7','8', '9','0']
    vowels = ['a','e','i','o','u']
    head = ''
    tail = ''
    for letter in word:
        if letter in consonants:
           head += letter
        else:
           cut = word.index(letter)
           tail = word[cut:len(word)]
           break
    return (head, tail)

#---------------------------------------------------
def test_stemmer():
    """ test stemmer """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')

# --------------------------------------------------
def main():

    args = get_args()
    pre = list('bcdfghjklmnpqrstvwxyz') +(
    'bl br ch cl cr dr fl fr gl gr pl pr sc '
    'sh sh sl sm sn sp st sw th tr tw thw wh wr'
    'sch scr shr sph spl spr squ str thr').split()

    word = args.word
    head, tail = stemmer(word)
    rhymes = []
    if tail:
       for prefix in pre:
           rhymes.append(prefix + tail)
       print(rhymes)
    else:
       print(f'Cannot rhyme "{args.word}"')
 
# --------------------------------------------------
if __name__ == '__main__':
    main()
