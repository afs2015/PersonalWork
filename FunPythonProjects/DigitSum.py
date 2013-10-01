#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to return a sum of a numbers digits

print ("Type digit_sum(number) to use this program.")

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

