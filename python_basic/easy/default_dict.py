# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
  
if __name__ == "__main__":
    a_size, b_size = map(int, input().split())
    a = defaultdict(list)
    b = list()
    
    for i in range(a_size):
        a[input()].append(i+1)
        
    for i in range(b_size):
        b.append(input())
    
    for i in b:

        if i in a:
            print(" ".join(map(str, a[i])))
        else:
            print(-1)
