# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        r = input()
        try:
            re.compile(r)
            print(True)
        except:
            print(False)