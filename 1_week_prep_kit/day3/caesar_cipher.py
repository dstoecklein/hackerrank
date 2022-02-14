#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    if k == 0:
        return s
    
    cipher = list()

    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            if c.islower():
                c = (ord(c) + k - 97) % 26 + 97
            else:
                c = (ord(c) + k - 65) % 26 + 65
            c = chr(c)
        cipher.append(c)
    return "".join(cipher)


if __name__ == '__main__':

    n = 11
    s = '159357lcfd'
    #159357fwzx
    k = 98

    result = caesarCipher(s, k)
    print(result)

