# Author: Andrew Selzer

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    total = 0
    for key in aDict:
        total += len(aDict[key])
    return total
