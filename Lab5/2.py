import re

word = "abbbaabbabbbbab"

print(re.findall("abbb|abb", word))