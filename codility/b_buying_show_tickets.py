
def buying(tickets, p):
    l = list()
    for i in range(len(tickets)):
        # simply take the minimum if alex's position less or equal current index
        # else same thing but minus 1 because they behind alex
        if i <= p:
            l.append(min(tickets[i], tickets[p]))
        else:
            l.append(min(tickets[i], tickets[p] - 1))

buying([2,6,3,4,5] ,2)