import re

word = str(input())

print(re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", word))