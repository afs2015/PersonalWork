#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: A basic version of the game battleship
# Version 1.0: Basic implmentation of battleship

# Imports
from random import randint

# Board creation
board = []

for x in range(5):
    board.append(["O"] * 5)

# Functions
def print_board(board):
    for row in board:
        print (" ".join(row))

def print_space():
    print ('\n')

# Game starts
print ("Let's play Battleship! \n")
print_board(board)
print_space()
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Generate 1x1 ship
ship_row = random_row(board)
ship_col = random_col(board)

#for debugging
#print (ship_row)
#print (ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(5):
    print ("You are on turn %d \n" % (turn+1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    print_space()

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship! \n")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean. \n")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.\n")
        else:
            print ("You missed my battleship! \n")
            board[guess_row][guess_col] = "X"
        if turn == 4:
            print ("Game Over \n")
        else:
            print_board(board)
