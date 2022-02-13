from collections import deque

# 0 left
# 1 right
def solution(weights, directions):
    if len(weights) != len(directions):
        return 0
    
    stack = []
    blue = 0

    for i in range(len(directions)):
        weight = weights[i]
        if directions[i] == 1:
            stack.append(weight)
        else:
            weightdown = stack.pop() if stack else -1 # only if not empty
            while weightdown != -1 and weightdown < weight:
                weightdown = stack.pop() if stack else -1
            if weightdown == -1:
                blue += 1
            else:
                stack.append(weightdown)
    return blue + len(stack)

print(solution([4,8,2,6,7], [0,1,1,0,0]))