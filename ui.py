from ComputerMode import *
import random

row = random.randint(1, 10)
col = row
matrix = initArr(row, col)


def commandInput():
    return input("Please input if you want to flip a row or column, \n and the index of the row or column: ")

def printBoard():
    for i in range(row+1):
        for j in range(col+1):
            print(matrix[i,j], end=" | ")
        print('\n')

def playerMode():
    printBoard()
    won = False
    while not won:
        cInput = commandInput()
        flipSign(matrix, cInput, row, col)
        won = checkWin(matrix, row, col)
    print("You have won")

def computerMode():
    printBoard()
    won = False
    while not won:
        print(hints(matrix, row, col))
        cInput = commandInput()
        flipSign(matrix, cInput, row, col)
        won = checkWin(matrix, row, col)
    print("You have won")


def description():
    print('There are 2 modes in this game 1) Player mode 2) Computer mode. \nIn player mode you can manually change the signs of the numbers in different rows and columns. \nIn Computer mode the computer will provide the user with the method to complete the game.')
    print('This is an sign-reversal puzzle game. You need to change the signs of the numbers in different rows and columns.The main goal of this game is to form a sum of rows and columns which is non-negative')
    menu()

def menu():
    print("Welcome to IDSA Matrix Game, Enter what you want to do: ")
    print("1. Play Player Mode")
    print("2. Play Computer Mode")
    print("3. Game description and how to play")
    choice = int(input())
    if(choice == 1):
        playerMode()
    elif(choice == 2):
        computerMode()
    elif(choice == 3):
        description()


menu()
