# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

l = list()
if __name__ == "__main__":
    s = input()
    for i, j in groupby(s):
        l.append((len(list(j)), int(i)))
    print(*l)