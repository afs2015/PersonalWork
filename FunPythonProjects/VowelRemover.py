#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to remove vowels from strings.

print ("Type anti_vowel(text) to use this program.")

def anti_vowel(text):
    anti_text = ""
    for letter in text:
        if not letter.lower() in "aeiou":
            anti_text += letter
    return anti_text