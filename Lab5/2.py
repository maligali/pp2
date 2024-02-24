import re

word = str(input())

print(re.findall("abbb|abb", word))