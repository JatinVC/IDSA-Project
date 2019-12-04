import numpy as np
m=3
n=3

def initArr(row, col):
    initedArr = np.random.randint(-10,10,(row, col))
    return initedArr

matrix = initArr(m, n)
print(matrix)
