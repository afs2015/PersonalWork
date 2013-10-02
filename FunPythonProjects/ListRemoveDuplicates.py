#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: Simple function to remove duplicate values from a list.

print ("Type remove_duplicates(List) to use this program.")

def remove_duplicates(List):
    newList = []
    for item in List:
        if item not in newList:
            newList.append(item)
    return newList

# Sample call: remove_duplicates([1,1,2,2])