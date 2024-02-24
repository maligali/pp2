import re
word =  str(input())
print((re.findall("[A-Z][^A-Z]*", word)))