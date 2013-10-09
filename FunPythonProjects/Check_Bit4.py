#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to check if a 4bit mask is on a provided integer. 

print ("Type check_bit4(num) to use this program.")
print ("Example: check_bit4(0b11011)")

def check_bit4(num):
    mask = 0b1000
    if (num & mask) > 0:
        return "on"
    else:
        return "off"