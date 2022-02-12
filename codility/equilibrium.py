def solution(arr):
    results = []
    left = 0
    right = 0
    for i in range(0, len(arr)):
        if i == 0:
            continue
        left = sum(arr[:i])
        right = sum(arr[i:])
        result = abs(left - right)
        results.append(result)
    
    return min(results)


if __name__ == '__main__':
    arr = [3,1,2,4,3]
    result = solution(arr)
    print(result)