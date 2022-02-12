# find the median

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr_sort = sorted(arr)
    m = int(len(arr) / 2)
    median = arr_sort[m]
    return median
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')



    arr = [0,1,2,4,6,5,3]

    result = findMedian(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
