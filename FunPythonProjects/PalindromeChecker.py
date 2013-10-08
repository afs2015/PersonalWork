#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to check if a string can be a palindrome, returns true or false.

def isPalindrome(word):
    return word == word[::-1]