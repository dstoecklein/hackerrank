import csv

def parse(csv_filename):
    d = dict()
    with open(csv_filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            d[row['id']] = row['count']

    return d

def print_count(data):
    print(data['Foobar'])

data = parse("codility/test.csv")
print_count(data)