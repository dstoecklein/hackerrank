# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N, M = map(int, input().split())
    
    counter = 1
    for i in range(N):

        if i < int(N/2):
            print((".|."*counter).center(M, "-"))
            counter += 2
        elif i > int(N/2):
            counter -= 2
            print((".|."*counter).center(M, "-"))
        else:
            print(("WELCOME").center(M, "-"))