from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()
    
    p = permutations(s, int(k))
    p = sorted(p)
    for i in p:
        print("".join(i))