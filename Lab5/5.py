import re

word = "Asbjqdbbaaabsssbaabaa"

print(re.findall("a.*b$", word))