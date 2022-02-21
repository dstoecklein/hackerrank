# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    
    
    for _ in range(n):
        a, b = input().split()
        
        try:
            result = int(a) / int(b)
            print(int(result))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)