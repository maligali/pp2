import re
word = str(input())
x = re.sub("_", "", word)
print(x)