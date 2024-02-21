a = int(input())
b = int(input())
def Square(a, b):
    for i in range(a, b + 1):
        yield i*i
Square_num = Square(a, b)
print (' '.join(map(str, Square_num)))