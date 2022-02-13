def solution(arr):

    candidate = 0
    counter = 0

    for a in arr:
        if counter == 0:
            candidate = a
            counter += 1
        elif candidate == a:
            counter += 1
        if candidate != a:
            counter -= 1
    
    occ = arr.count(candidate)

    if occ > (len(arr) / 2):
        return arr.index(candidate)
    else:
        return -1

print(solution([3,0,1,1,4,1,1]))