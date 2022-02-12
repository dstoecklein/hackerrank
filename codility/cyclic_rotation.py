def cyclic_rotation(arr, k):

    last = 0
    for _ in range(k):
        last = arr[len(arr)-1]
        arr = [last] + arr[:-1]
    return arr

print(cyclic_rotation([1,2,3,4,5], 2))
print(cyclic_rotation([1,2,3,4,5], 5))