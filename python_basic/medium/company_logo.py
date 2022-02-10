# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

chars = list("aabbbccde")
distinct_chars = len(list(dict.fromkeys(chars)))

if len(chars) > 3 and distinct_chars >= 3:
    results = Counter(chars).most_common(3)

    # or...
    # results = dict((i, chars.count(i)) for i in chars)
    # results = sorted(results.items(), key=lambda item: item[1], reverse=True)[:3]

    for r in results:
        print(r[0], r[1])