#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 3/4/2021
Purpose: Bottles of Beer Song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottle of Beer Song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

def verse(bottle):
    """ Sing a verse """
    nextbottle = bottle-1
    s1 = ''
    s2 = ''
    if bottle == 1:
        s1 = ''
    else:
        s1='s'
    if nextbottle == 1:
        s2 = ''
    else:
        s2 = 's'
    if nextbottle == 0:
        nextnumber = 'No more'
    else:
        nextnumber = nextbottle

    return '\n'.join([f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,', 
        f'Take one down, pass it around,',
        f'{nextnumber} bottle{s2} of beer on the wall!']) 
    
    

def test_verse():
    """ Test verse """
    last_verse = verse(1)
    assert last_verse == '\n'.join(['1 bottle of beer on the wall',
        '1 bottle of beer,', 'Take one down, pass it around,',
        'No more bottles of beer on the wall!'])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join(['2 bottles of beer on the wall',
        '2 bottles of beer,', 'Take one down, pass it around,',
        '1 bottles of beer on the wall!'])
# --------------------------------------------------
def main():

    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
