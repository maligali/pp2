print("Hey")
#is the same as
print('Hey')

#assign string to a variable
a = "Hi"
print(a)

#Multiline strings
#three double quotes
a = """V lesu rodilas yelochka
V lesu ona rosla
Zimoi i letom stroynaya
zelyonaya byla."""
print(a)
#or three single quotes
a = '''V lesu rodilas yelochka
V lesu ona rosla
Zimoi i letom stroynaya
zelyonaya byla.'''
print(a)

#strings as arrays
a = "Hello, World!"
print(a[0])

#Looping Through a String
for x in "cherry":
  print(x)

#string length
a = "Goodbye, teacher!"
print(len(a))

#check string
txt = "The best thing in life is money!"
print("money" in txt)
txt = "The best thing in life is money!"
if "money" in txt:
  print("Yes, 'money' is present.")

#if not
txt = "The best thing in life is money!"
print("free" not in txt)
txt = "The best thing in life is money!"
if "free" not in txt:
  print("No, 'free' is NOT present.")
