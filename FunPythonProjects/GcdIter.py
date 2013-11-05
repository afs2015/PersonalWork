#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to return the gcd of two positive integers in an iterative manner

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testVal = 0
    if (a > b):
        testVal = a
    else:
        testVal = b
    while (testVal != 0):
        if (a % testVal == 0 and b % testVal == 0):
            return testVal
        else:
            testVal -= 1