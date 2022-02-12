def max_counters(k, arr):
    arr_tmp = [0]*k

    for i in range(len(arr)):
        if arr[i] > len(arr_tmp):
            arr_tmp = [max(arr_tmp)]*k
        else:
            arr_tmp[arr[i]-1] += 1
    print(arr_tmp)


max_counters(5, [3,4,4,6,1,4,4])