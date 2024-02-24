import re

word = str(input())

print(re.findall("ab*", word))