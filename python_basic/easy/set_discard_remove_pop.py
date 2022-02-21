n = int(input())
s = set(map(int, input().split()))
c = int(input())

for i in range(c):
    command = input().split()
    
    if len(command) == 1:
        if command[0] == "pop":
            s.pop()
        continue
    
    operation = command[0]
    element = int(command[1])
    
    if operation == "remove":
        s.remove(element)
    elif operation == "discard":
        s.discard(element)
        
print(sum(s))