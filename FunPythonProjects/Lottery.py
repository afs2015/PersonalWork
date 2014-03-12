import random

# Read a file
with open("sort.txt.", "r+") as fo:
	text = fo.readlines()

def list_append_from_file(file):
	'''
	inputs: file
	output: strips newlines and adds each line from file into list
	'''
	for line in file:
		line = line.rstrip("\n")
		entries.append(line)

# list to hold winners
entries = []

list_append_from_file(text)

#print winner
print(random.choice(entries))

fo.close()
