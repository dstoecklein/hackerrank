# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m1 = int(input())
    s1 = set(list(map(int, input().split())))
    m2 = int(input())
    s2 = set(list(map(int, input().split())))
    
    a = s1.difference(s2)
    b = s2.difference(s1)
    result = a.union(b)
    print ('\n'.join(map(str, sorted(result, key=int))))