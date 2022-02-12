#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = int(len(matrix)/2)
    suma = 0
    for i in range(n):
        for j in range(n):

            suma += max(
                max(matrix[i][j],
                matrix[2*n-i-1][j]),
                max(matrix[i][2*n-j-1],
                matrix[2*n-i-1][2*n-j-1])
            )
    return suma

if __name__ == '__main__':
    n = 1
    matrix = [
            [112, 42, 83, 119], 
            [56, 125, 56, 49], 
            [15, 78, 101, 43], 
            [62, 98, 114, 108]
            ]
    matrix2 = [[1,2], [3, 4]]
    result = flippingMatrix(matrix)
    print(result)
