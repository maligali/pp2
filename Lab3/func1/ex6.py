def rev(s):
    x = s.split(" ")
    x.reverse()
    return ' '.join(x)
s = str(input())
print(rev(s))