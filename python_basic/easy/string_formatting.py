def print_formatted(number):
    padding = len(str(format(number, "b")))
    for i in range(1, number+1):
        print ("{0:{padding}d} {0:{padding}o} {0:{padding}X} {0:{padding}b}".format(i, padding=padding))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)