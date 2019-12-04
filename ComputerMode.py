import numpy as np
m=3
n=3

def initArr(row, col):
    initedArr = np.random.randint(-10,10,(row, col))
    return initedArr
    print("Sum of each row:\n")


matrix = initArr(m, n)
print(matrix)

def sums(arr):
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += arr[i][j]
        print("sum of row ", i, "=", sum)
        sum = 0

    for i in range(3):
        sum = 0
        for j in range(3):
            sum += arr[j][i]
        print("sum of col ", i, "=", sum)
        sum = 0

sums(matrix)
