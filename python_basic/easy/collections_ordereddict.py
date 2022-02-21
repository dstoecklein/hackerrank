# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    words = list()
    
    for i in range(n):
        words.append(input())
        
    distinct = len(set(words))

    o = OrderedDict()
    
    for w in words:
        if w in o:
            o[w] += 1
        else:
            o[w] = 1
            
    print(distinct)
    result = ""
    for k, v in o.items():
        result += str(v) + " "
    print(result)