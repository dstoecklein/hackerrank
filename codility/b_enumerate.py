def en(seq):
    l = list()  
    for i, s in enumerate(seq):
        l.append((i, s))
    print(l)

en(['Spring', 'Summer', 'Fall', 'Winter'])