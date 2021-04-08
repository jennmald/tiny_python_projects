#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 4/8/2021
Purpose: Mad Libs: Using Regular Expressions
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
			 metavar = 'FILE',
			 type = argparse.FileType('rt'),
			 help = 'Input file')

    parser.add_argument('-i',
                        '--inputs',
			nargs  = '*',
                        help = 'Inputs (for testing)',
                        metavar='input',
                        type = str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    blank = re.findall('(<([^<>]+)>)', text)
    
    if not blank:
      sys.exit(f'"{args.file.name}" has no placeholders.')

    tmpl = 'Give me {} {}: '
    for p, pos in blank:
        article = 'an' if pos.lower()[0] in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, pos))
        text = re.sub(p, answer, text, count=1)

    print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()
