import re

word = str(input())

print(re.findall(r"[A-Z][a-z]*", word))