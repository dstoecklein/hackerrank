#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_list = s.split(" ")

    new_s = ""
    for i in range(0, len(s_list)):
        if len(new_s) == 0:
            new_s = s_list[i].capitalize()
        else:
            new_s = new_s + ' ' + s_list[i].capitalize()
    return new_s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
