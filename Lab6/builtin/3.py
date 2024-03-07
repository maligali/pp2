str = str(input())
str = str.lower().replace(" ", "")
rev = ''.join(reversed(str))
if rev == str:
    print ("Yes, the string is palindrome")
else: 
    print ("No, the string is not palindrome")