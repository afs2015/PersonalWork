#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function that flips a bit of a provided integer and bit.

print ("Type flip_bit(number,n) to use this program.")
print ("Example: flip_bit(0b10,2)")


def flip_bit(number,n):
    mask = (0b1 << n-1)
    return bin(number ^ mask)