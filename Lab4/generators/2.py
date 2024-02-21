n = int(input())
def Even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
even_num = Even(n)
print(', '.join(map(str, even_num)))