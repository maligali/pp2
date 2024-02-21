n = int(input())
def Square(n):
    for i in range(n + 1):
        yield i*i
Square_num = Square(n)
print (' '.join(map(str, Square_num)))