if __name__ == '__main__':
    s = "qA2"

    isalnum = 0
    isalpha = 0
    isdigit = 0
    islower = 0
    isupper = 0


    for c in s:
        if c.isalnum():
            isalnum += 1
        if c.isalpha():
            isalpha += 1
        if c.isdigit ():
            isdigit += 1
        if c.islower():
            islower += 1
        if c.isupper():
            isupper += 1
        
    
    print(True if isalnum > 0 else False)
    print(True if isalpha > 0 else False)
    print(True if isdigit > 0 else False)
    print(True if islower > 0 else False)
    print(True if isupper > 0 else False)