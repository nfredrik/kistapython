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
    word_list = []
    with open('sowpods.txt', 'r') as sowpods:
#    with open('psowpods.txt', 'r') as sowpods:
        word_list = sowpods.read().lower().strip().splitlines()

    # print word_list[-1]

    # Get the rack

    parser = argparse.ArgumentParser(description='Scrabble cheater.')

    parser.add_argument('nisse', action="store",  help='a word', nargs='+')

    args = parser.parse_args()

    #print args
    rack_letters = []
    for i in  args.nisse:
        if re.match('[a-zA-Z]+',i):
            rack_letters.append(i.lower())
        else:
            print "Not valid word", i

    print rack_letters
    # Find valid word_list

    valid_words = []

    #for cc in rack_letters:

    #print word_list[0]
    """

    https://openhatch.org/wiki/Scrabble_challenge

    Write the code to find all words from the word_list that are made of letters
    that are a subset of the rack_letters. 

    There are many ways to do this, but here's one way that is easy to reason about
    and is fast enough for our purposes: 

    go through every word in the word_list, and for every letter in that word, see if
    that letter is  contained in the rack. If it is, save the word in a valid_words list.
    Make sure you  handle repeat letters: once a letter from the rack has been used, 
    it can't be used again.
    """





    for word in word_list:                         # get a word from the dictionary
        cntr = 0 
        rack = list(rack_letters[0])

        for r_letter in rack:                      # get a letter from the rack word

            for letter in word:                         # get a letter of the word     
#                print letter,r_letter, idx  
                if letter == r_letter:                   # letter from word in rack word?
#                    print rack
                    rack.pop()
                    cntr+=1
#                    break

            if len(word) == cntr:                  # if all letter in word matches rack store it
#               print 'addin', word
                valid_words.append(word)

#    print len(valid_words)

    for i in valid_words:
        print i
                           
                    
    # Scoring


    return 0



if __name__ == '__main__':
    
    sys.exit(main())
