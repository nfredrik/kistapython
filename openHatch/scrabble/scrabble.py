#!/usr/bin/env python

import re
import sys
import argparse

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def main():

    # Contruct a word list
    words = []
    with open('sowpods.txt', 'r') as sowpods:
        words = sowpods.read().strip().splitlines()

    # print words[-1]

    # Get the rack

    parser = argparse.ArgumentParser(description='Scrabble cheater.')

    parser.add_argument('nisse', action="store",  help='a word', nargs='+')
#    parser.add_argument('integers', metavar='N', type=int, nargs='+',  help='an integer for the accumulator')
#   parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,help='sum the integers (default: find the max)')

    args = parser.parse_args()

    #print args
    valid_list = []
    for i in  args.nisse:
        if re.match('[a-zA-Z]+',i):
            valid_list.append(i.lower())
        else:
            print "Not valid word", i

    print valid_list
    # Find valid words

    valid_words = []

    #for cc in valid_list:
    
    for w in words:
        for l in w:
           for x, y in enumerate(valid_list[0])
               if l == y:
                   valid_list.pop(x)
                           
                    
    # Scoring


    return 0



if __name__ == '__main__':
    
    sys.exit(main())
