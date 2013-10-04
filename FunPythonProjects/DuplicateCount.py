#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Function to count the number of duplicate values from a string.

print ("Type duplicateCount(input) to use this program.")
print ("Example: duplicateCount([1,2,2,2,3,3,3])")

# This works by reading a string a single character at a time and appending it to a variable.
def duplicateCount(lst):
    newList = []
    count = 0
    for item in lst:
        if item in newList and newList.count(item) < 2:
                count += 1
                newList.append(item)
        else:
        	newList.append(item)
    return count
