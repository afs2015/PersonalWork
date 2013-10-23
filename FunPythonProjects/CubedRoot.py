#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function that finds the cubed root of a provided integer

print ("Type cubedRoot(number) to use this program.")

def cubedRoot(num):
	ans = 0
	for ans in range(0, abs(num)+1):
		if ans**3 == abs(num):
			break
	if (ans**3 != abs(num)):
		return str(num) + " is not a perfect cube"
	elif (num < 0):
		ans = -ans
		return "The cubed root is " + str(ans)
	else:
		return "The cubed root is " + str(ans)
