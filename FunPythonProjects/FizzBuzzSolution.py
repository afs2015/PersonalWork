#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Sample FizzBuzz solution. Counts from 1-100 and prints Fizz if number is divisible by 3, Buzz if number is divisible by 5

for num in range(1,101):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    print (msg or num)
