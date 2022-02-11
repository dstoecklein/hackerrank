def print_formatted(number):
    # your code goes here
    padding = len(format(number, "b"))-1
    for i in range(number):
        print(
            format(number),
            " " * padding,
            format(number, "o"),
            " " * padding,
            format(number, "x"),
            " " * padding,
            format(number, "b"),
        )
    

if __name__ == '__main__':
    n = int(17)
    print_formatted(n)