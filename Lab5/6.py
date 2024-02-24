import re
word = str(input())
x = re.sub('[ ,.]', ':', word)
print(x)