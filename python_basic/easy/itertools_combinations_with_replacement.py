# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, i = input().split()
    
    p = sorted(list(s))
    p = list(combinations_with_replacement(p, int(i)))
    for t in p:
        print("".join(t))