# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    n = int(input())
    
    
    d = deque()
    
    for i in range(n):
        
        l = list(input().split())

        if len(l) == 1:
            method = l[0]
        else:
            method, value = l
            
        if method == "append":
            d.append(int(value))
        elif method == "pop":
            d.pop()
        elif method == "popleft":
            d.popleft()
        elif method == "appendleft":
            d.appendleft(int(value))
    print(*d)
