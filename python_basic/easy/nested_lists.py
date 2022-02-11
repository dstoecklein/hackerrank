if __name__ == '__main__':
    
    names = list()
    scores = list()
    arrays = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arrays.append([name, score])
        scores.append(score)
    
    # sorting
    arrays = sorted(arrays, key=lambda x:x[1])
    second_lowest = sorted(set(scores))[1]
    
    # check occurrences
    occurrences = scores.count(second_lowest)
    
    # get items
    if occurrences >= 2:
        for arr in arrays:
            if arr[1] == second_lowest:
                names.append(arr[0])
        names = sorted(names)[:2]
        print(*names, sep="\n")
    else:
        for arr in arrays:
            if arr[1] == second_lowest:
                names = arr[0]
                break
        print(names)
        