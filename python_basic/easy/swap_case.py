def swap_case(s):
    l = list()
    for c in s:
        if c.isupper():
            c = c.lower()
        elif c.islower():
            c = c.upper()
        l.append(c)
    return "".join(l)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)