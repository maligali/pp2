import re
word = str(input())
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', word)
print(x)