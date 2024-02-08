from itertools import permutations
def per(s):
    list = [''.join(p) for p in permutations(s)]
    return list

s = str(input())

print(per(s))