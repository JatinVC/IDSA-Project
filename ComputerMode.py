import numpy as np

def initArr(row, col):
    sumPosCount = 0
    initedArr = np.random.randint(-10,10,(row+1, col+1))
    #adding row and column for sum
    initedArr[:][row] = 0
    initedArr[:,col] = 0
    updateSums(initedArr, row, col)
    for i in range(row):
        if initedArr[i, col]>-1:
            sumPosCount+=1
        elif initedArr[row, i]>-1:
            sumPosCount+=1
    if (sumPosCount == ((row*2)-1)):
        return initArr(row, col)
    return initedArr

def updateSums(arr, row, col):
    sum = 0
    #row sum
    for i in range(row):
        for j in range(col):
            sum += arr[i][j]
        arr[i,col] = sum
        sum = 0
    #col sum
    for i in range(col):
        for j in range(col):
            sum += arr[j][i]
        arr[row,i] = sum
        sum = 0

    for i in range(row+1):
        for j in range(col+1):
            print(arr[i,j], end=" | ")
        print('\n')


def flipSign(arr, cInput, row, col):
    command = cInput.split()
    index = int(command[1]) - 1
    if(command[0].lower() == "row"):
        arr[:][index] *= -1
        updateSums(arr, row, col)
    elif(command[0].lower() == "col"):
        arr[:, index] *= -1
        updateSums(arr, row, col)
    else:
        print("invalid input, please try again")

def checkWin(arr, row, col):
    rowPos = False
    colPos = False
    for i in range(row):
        if arr[i, col] > 0:
            colPos = True
        else:
            colPos = False
            break
    for i in range(col):
        if arr[row, i] > 0:
            rowPos = True
        else:
            rowPos = False
            break
    if (rowPos == True and colPos == True):
        return True

def hints(arr, row, col):
    #check if row sum is non-negative, if its negative, then suggest player to reverse sign
    for i in range(row):
        if arr[i,col] < 0:
            return "I would recommend flipping row: " + str(i+1)
    #check if col sum is non-negative, if its negative, then suggest player to reverse sign
    for i in range(col):
        if arr[row,i]<0:
            return "I would recommend flipping col: " + str(i+1)
    else:
        #if no changes
        return "You have won"
