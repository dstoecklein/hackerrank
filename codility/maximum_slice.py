def solution(arr):
    global_max = 0
    local_max = 0

    for i in range(1, len(arr)):
        delta = arr[i] - arr[i - 1]
        local_max = max(delta, local_max + delta)
        global_max = max(local_max, global_max)
    return global_max 

print(solution([5,-4,8,-10,-2,4,-3,2,7,-8,3,-5,3]))