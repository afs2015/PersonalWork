#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to use reverse a string. 

print ("Type reverse(text) to use this program.")

# This works by reading a string a single character at a time and appending it to a variable.
def reverse(text):
    a=""
    for i in text:
        a=i+a
    return a