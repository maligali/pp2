import re

word = str(input())

print(re.findall("a.*b$", word))