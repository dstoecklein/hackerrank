# split by " "
# join by -

def split_and_join(line):
    l = list()
    l = line.split(" ")
    return "-".join(l)

if __name__ == '__main__':
    line = "this is a string"
    result = split_and_join(line)
    print(result)