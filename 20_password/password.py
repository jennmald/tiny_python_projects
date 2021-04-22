#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 4/22/2021
Purpose: Password Strength
"""

import argparse
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password Strength',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--num',
                        metavar='num_passwords',
                        type = int,
                        default = 3,
                        help='Number of passwords to generate')

    parser.add_argument('file',
                         metavar = 'FILE',
                         type = argparse.FileType('rt'),
                         nargs = '+',
                         help = 'Input files(s)')
    
    parser.add_argument('-w', '--num_words',
                         metavar = 'num_words',
                         type = int,
                         default = 4,
                         help = 'Number of words to use for password')
    
    parser.add_argument('-m', '--min_word_len',
                         metavar = 'minimum', 
                         type = int,
                         default = 3,
                         help = 'Minimum word length')

    parser.add_argument('-x', '--max_word_len',
                         metavar = 'maximum', 
                         type = int,
                         default = 6,
                         help = 'Maximum word length')

    parser.add_argument('-s', '--seed',
                        metavar = 'seed',
                        type = int,
                        help = 'Random seed')

    parser.add_argument('-l',
                        '--l33t',
                        action = 'store_true',
                        help='Obfuscate letters')

    return parser.parse_args()


# --------------------------------------------------
def clean(word):
    # Remove non-word characters from a word
    return re.sub('[^a-zA-Z]', '', word)


# --------------------------------------------------
def l33t(text):
    # obfuscate password using ransom method
    text = ransom(text)
    xform = str.maketrans({'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


# --------------------------------------------------
def ransom(text):
   # randomly choose upper or lowercase letters to return
   return ''.join(map(lambda c: c.upper() if random.choice([0,1]) else c.lower(), text))


# --------------------------------------------------
def test_clean():
    # Test clean method
    assert clean('') == ''
    assert clean("states,") == 'states'
    assert clean("Don't") == 'Dont'


# --------------------------------------------------
def test_l33t():
    state = random.getstate()
    random.seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'D0ll4r5`'
    random.setstate(state)

# --------------------------------------------------
def test_ransom():
   state = random.getstate()
   random.seed(1)
   assert ransom('Money') == 'moNeY'
   assert ransom('Dollars') == 'DOLlaRs'
   random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    # determine if word is in correct length requirements
    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
       for line in fh:
          for word in filter(word_len, map(clean, line.lower().split())):
              words.add(word.title())
    
    words = sorted(words)
    passwords = [ ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
                ]
   
    if args.l33t:
       passwords = map(l33t, passwords)

    print('\n'.join(passwords))


# --------------------------------------------------
if __name__ == '__main__':
    main()
