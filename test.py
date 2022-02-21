from itertools import groupby

s1 = "aabbcdefg"
s2 = "gfedcba"

for key, group in groupby(s1):
    print(key, list(group))