#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to check if a string can be a palindrome. If it is assemble it.

from collections import deque, Counter


def palindrome_from(letters):
    counter = Counter(letters)
    sides = []
    center = deque()
    for letter, occurrences in counter.items():
        repetitions, count = divmod(occurrences, 2)
        if not count:
            sides.append(letter * repetitions)
            continue
        if center:
            return -1
        center.append(letter * occurrences)
    center.extendleft(sides)
    center.extend(sides)
    return ''.join(center)
