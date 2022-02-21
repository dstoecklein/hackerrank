# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())

    o = OrderedDict()
    
    for i in range(n):
        items = list(input().split())
        net_price = int(items[-1])
        item_name = " ".join(items[:-1])
        if item_name in o:
            o[item_name] += net_price
        else:
            o[item_name] = net_price
            
    for k, v in o.items():
        print(k, v)