#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/5/2021
Purpose: Twelve Days of Christmas
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    args = parser.parse_args()
    if args.num<1 or args.num>12:
       parser.error(f'error: --num "{args.num}" must be between 1 and 12')
    return parser.parse_args()

def sing(num):
   """ Create a verse """
   ordinal = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth',
              6:'sixth', 7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth',
              11:'eleventh', 12:'twelfth'}

   given = ['And a partridge in a pear tree.', 'Two turtle doves,',
            'Three French hens,','Four calling birds,', 'Five gold rings,',
            'Six geese a laying,','Seven swans a swimming,',
            'Eight maids a milking,', 'Nine ladies dancing,',
            'Ten lords a leaping,', 'Eleven pipers piping,',
            'Twelve drummers drumming,']

   begin = 'On the ' + ordinal[num] + ' day of Christmas,'
   love = 'My true love gave to me,'
   verse = []
   for day in range(0,num):
       if num == 1:
          verse.append('A partridge in a pear tree.')
       else:
          verse.append(given[day])
   verse.reverse()
   verse.insert(0, begin)
   verse.insert(1, love)
   return verse


def test_sing():
   """ Simple test for the verse function """
   assert sing(1) == ['On the first day of Christmas,',
        'My true love gave to me,', 'A partridge in a pear tree.']
   assert sing(2) == ['On the second day of Christmas,',
        'My true love gave to me,', 'Two turtle doves,',
        'And a partridge in a pear tree.']

# --------------------------------------------------
def main():
    """Return the song as days given by user"""
    args = get_args()
    day = args.num
    for d in range(1, day+1):
    	song  = sing(d)
    	for line in song:
           print(line)

# --------------------------------------------------
if __name__ == '__main__':
    main()
