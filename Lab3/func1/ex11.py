def palindrome(s):
    r = s[::-1]
    return s == r

print(palindrome("madam"))
print(palindrome("mama"))