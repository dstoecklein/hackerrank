# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    s = set()
    for i in range(n):
        c = input()
        s.add(c)
    print(len(s))