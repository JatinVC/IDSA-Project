import numpy as np

def initArr(row, col):
    sumPosCount = 0
    initedArr = np.random.randint(-10,10,(row+1, col+1))
    #adding row and column for sum
    initedArr[:][row] = 0
    initedArr[:,col] = 0
    updateSums(initedArr, row, col)
    for i in range(row):
        if initedArr[i, col]>0:
            sumPosCount+=1
        elif initedArr[row, i]>0:
            sumPosCount+=1
    if sumPosCount == (row*2):
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
        
def choose(arr, row, col):
    #row inverse
    for i in range(row):
        for j in range(col):
            varname[:][row] *= -1
        arr[i,col] = sum
        sum = 0
    #col inverse
    for i in range(row):
        for j in range(col):
            varname[:,col] *= -1
        arr[row,j] = sum
        sum = 0

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
