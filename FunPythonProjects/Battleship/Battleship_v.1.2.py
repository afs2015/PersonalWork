#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: A basic version of the game battleship

# Version 1.0: 
#   Basic implmentation of battleship
# Version 1.1: 
#   Added error handling and returns coordinates of ship upon game over.
# Version 1.2: 
#   Moved the check for if the ship was sunk and the check for ocean bounds to functions.
#   Added how many turns it took the user to win the game.

# Imports
from random import randint

# Board creation
board = []

for x in range(5):
    board.append(["O"] * 5)

# Functions

# Prints the game board
def print_board(board):
    for row in board:
        print (" ".join(row))

# Prompts the user for a row guess
def get_row():
    while True:
        try:
            return int(input("Guess Row:"))
        except ValueError:  #if the user didn't enter a number
            print ("A valid row wasn't entered! Please enter a number between 0 and 5. \n")

# Prompts the user for a column guess
def get_col():
    while True:
        try:
            return int(input("Guess Col:"))
        except ValueError:  #if the user didn't enter a number
            print ("A valid column wasn't entered! Please enter a number between 0 and 5. \n")

# Generates a ship on a random row
def random_row(board):
    return randint(0, len(board) - 1)

# Generates a ship on a random column
def random_col(board):
    return randint(0, len(board[0]) - 1)

# Checks if the user has sunk the ship
def ship_check():
    if guess_row == ship_row and guess_col == ship_col:
        return True
    else:
        return False

# Checks if user's guess is in the game boundries (ocean)
def ocean_bounds_check():
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        return True
    else:
        return False

# Game starts
print ("Let's play Battleship! \n")
print_board(board)

# Generate 1x1 ship
ship_row = random_row(board)
ship_col = random_col(board)

#for debugging
print (ship_row)
print (ship_col)

for turn in range(5):
    print ("You are on turn %d \n" % (turn+1))
    
    # Prompts user for guesses
    guess_row = get_row()
    guess_col = get_col()

    if (ship_check()):
        if (turn+1) == 1:
            print ("Congratulations! You sunk my battleship! It took you %s turn.\n" % (turn+1))
            break
        else:
            print ("Congratulations! You sunk my battleship! It took you %s turns.\n" % (turn+1))
            break
    else:
        if (ocean_bounds_check()):
            print ("Oops, that's not even in the ocean. \n")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.\n")
        else:
            print ("You missed my battleship! \n")
            board[guess_row][guess_col] = "X"
        if turn == 4:
            print ("Game Over, the ship was at row %s and column %d \n" % (ship_row, ship_col))
        else:
            print_board(board)
