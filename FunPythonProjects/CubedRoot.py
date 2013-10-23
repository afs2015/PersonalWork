#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function that finds the cubed root of a provided integer

print ("Type cubedRoot(number) to use this program.")

def cubedRoot(num):
	ans = 0
	while (ans**3 < abs(num)):
		ans += 1
	if (ans**3 != abs(num)):
		return str(num) + " is not a perfect cube"
	else:
		return "The cubed root is " + str(ans)
