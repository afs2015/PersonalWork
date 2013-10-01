#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to use recursion to find the factorial of a number.

print ("Type factorial(number) to use this program.")

def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x-1)