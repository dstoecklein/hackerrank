#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print("{:.6f}".format(pos / len(arr)))
    print("{:.6f}".format(neg / len(arr)))
    print("{:.6f}".format(zero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
