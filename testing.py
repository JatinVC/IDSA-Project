from ComputerMode import *

rowInput = int(input("Enter how many rows in the game"))
colInput = int(input("Enter how many columns in the game"))

matrix = initArr(rowInput, colInput)
updateSums(matrix,rowInput,colInput)
print(matrix)
print(hints(matrix, rowInput, colInput))
