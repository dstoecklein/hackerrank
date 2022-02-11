if __name__ == '__main__':
    n = int(5)
    arr = [2,3,6,6,5]
    
    arr = sorted(set(arr))[-2]
    print(arr)