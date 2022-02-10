if __name__ == '__main__':
    n = int(input())
    result = list()
    if n <= 1:
        print(n)
    else:
        for i in range(n):
            result.append(i+1)
    result = list(map(str, result))
    print("".join(result))