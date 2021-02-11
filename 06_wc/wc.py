#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Word Count
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word Count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs = '*',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for filename in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in filename:
            num_lines+=1
            words = line.split()
            num_words += len(words)
            num_bytes += len(line)
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {filename.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')
# --------------------------------------------------
if __name__ == '__main__':
    main()
