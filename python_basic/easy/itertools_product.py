A = [1,2]
B = [3,4]

result = list()
for a in A:
    for b in B:
        result.append((a, b))
print(*result)

# or...
from itertools import product
print(*product(A,B))