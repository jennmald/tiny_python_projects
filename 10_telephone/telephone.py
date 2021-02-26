#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/26/2021
Purpose: Telephone: Randomly mutating strings
"""

import argparse
import random
import string
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # maybe a text arguement or a file name
    parser.add_argument('text',
                        metavar='str',
                        type = str,
                        help='Input string or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='A floating point between 0 and 1',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if args.mutations > 1 or args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    # check if text is name of file
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    # get arguements
    args = get_args()
    text = args.text
    mutations = args.mutations
    random.seed(args.seed)
    # compute number of mutations
    num_mutations = round(len(text)*mutations)
    # create an ASCII alphabet
    alphabet = ''.join(sorted(string.ascii_letters + string.punctuation))
    # copy to mutate
    heard_text = text
    for i in random.sample(range(len(text)), num_mutations):
        char = random.choice(alphabet.replace(heard_text[i],''))
        heard_text = heard_text[:i]+char+heard_text[i+1:]

    print(f'You said: "{text}"')
    print(f'I heard : "{heard_text}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
