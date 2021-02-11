#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Going on a Picnic
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Going on a Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    items = args.item

    if args.sorted:
        items.sort()

    picnic_items = ''
    if len(items) == 1:
        picnic_items = items[0]
    elif len(items) == 2:
        picnic_items = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        picnic_items = ', '.join(items)

    print('You are bringing {}.'.format(picnic_items))

# --------------------------------------------------
if __name__ == '__main__':
    main()
