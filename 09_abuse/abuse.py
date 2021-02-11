#!/usr/bin/env python3
"""
Author : Jennefer Maldonado
Date   : 2/11/2021
Purpose: Dial-a-Curse
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Dial-a-Curse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of Adjectives (default:2)',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of Insults(default:3)',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed (default:None)',
                        metavar='seed',
                        type=int,
                        default=None)
    args = parser.parse_args()
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    return args


# --------------------------------------------------
def main():
    adject = ['bankrupt', 'base', 'caterwauling', 'corrupt', 'cullionly', 'detestable', 'dishonest', 'false',
                 'filthsome', 'filthy','foolish', 'foul', 'gross', 'heedless', 'indistinguishable', 'infected',
                 'insatiate', 'irksome', 'lascivious', 'lecherous', 'loathsome', 'lubbery', 'old', 'peevish', 
                 'rascaly', 'rotten', 'ruinous', 'scurilous', 'scurvy', 'slanderous', 'sodden-witted',
                 'thin-faced', 'toad-spotted', 'unmannered', 'vile', 'wall-eyed']

    nouns = ['Judas', 'Satan', 'ape', 'ass', 'barbermonger', 'beggar', 'block', 'boy', 'braggart', 'butt',
             'carbuncle', 'coward', 'coxcomb', 'cur', 'dandy', 'degenerate', 'fiend', 'fishmonger', 'fool',
             'gull', 'harpy', 'jack', 'jolthead', 'knave', 'liar', 'lunatic', 'maw', 'milksop', 'minion',
             'ratcatcher', 'recreant', 'rogue', 'scold', 'slave', 'swine', 'traitor', 'varlet', 'villain', 'worm']

    args = get_args()
    num_i = args.number
    random.seed(args.seed)

    for a in range(0, num_i):
        insults = ', '.join(random.sample(adject, k=args.adjectives))
        print('You '+insults+ ' ' + random.choice(nouns) +'!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
