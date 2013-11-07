#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Pig Latin Transltor

pyg = 'ay'

original = input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in 'aeiou':
        new_word = word + 'ay'
        print (new_word)
    else:
        first_letter = word[0]
        new_word = word[1:]
        new_word = new_word + first_letter + 'ay'
        print (new_word)
else:
    print ('empty')
