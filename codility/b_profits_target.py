from numpy import sort

import itertools

# == Bad solution, 3x loops ==

def profit_target(profits, target):
    pairs = []

    for i in profits:
        for _, j in enumerate(profits, 1):
            if (i + j) == target:
                pairs.append(sorted([i, j]))
    pairs.sort()
    pairs = list(k for k, _ in itertools.groupby(pairs))
    return len(pairs)

profit_target([5,7,9,13,11,6,6,3,3], 12)