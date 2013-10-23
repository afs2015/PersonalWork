#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function that sums all numbers for a provided integer
# Example: 5 would return 1 + 2 + 3 + 4 + 5 a.k.a., 15

print ("Type summation(number) to use this program.")

def summation(num):
        counter = 1
        tot = 0

        while (counter <= num):
                tot += counter
                counter += 1
        return tot
