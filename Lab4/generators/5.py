n = int(input())
def Down(n):
    for i in range(n, -1, -1):
        yield i
down = Down(n)
print(' '.join(map(str, down)))