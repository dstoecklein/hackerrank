# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    words = list()
    
    for i in range(n):
        words.append(input())
        
    distinct = len(set(words))
    