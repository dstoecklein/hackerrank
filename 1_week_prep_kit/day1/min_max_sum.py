#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = sorted(arr)[0:-1]
    max = sorted(arr, reverse=True)[0:-1]
    print(sum(min), sum(max))
    
if __name__ == '__main__':

    arr = [1,3,5,7,9]

    miniMaxSum(arr)
