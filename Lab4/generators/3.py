n = int(input())
def Twelve(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
twelve = Twelve(n)
print (' '.join(map(str, twelve)))