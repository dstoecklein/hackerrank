# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    _shoes = Counter(list(map(int, input().split())))
    customers = int(input())
    
    earned = 0
    
    for c in range(customers):
        size, price = list(map(int, input().split()))
        
        if size in _shoes:
            if _shoes[size] > 0:
                _shoes[size] -= 1
                earned += price
    print(earned)
        