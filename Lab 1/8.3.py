#String Concatenation
a = "Four"
b = "Three"
c = a + b
print(c) #FourThree

a = "Four"
b = "Three"
c = a + " " + b
print(c) #Four Three

#String format
'''We canNOT combine strings and numbers like this:
age = 99
a = "I am Sean, I am " + age
print(a)'''

#we can use the format() method

age = 99
a = "My name is Sean, and I am {}"
print(a.format(age))

numberofpieces = 10
number = 646
price = 99
iwant = "I want {} loafs of bread {} for {} tenge."
print(iwant.format(numberofpieces, number, price))

#you can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
numberofpieces = 10
number = 646
price = 99
iwant = "I want {0} loafs of bread {1} for {2} tenge."
print(iwant.format(numberofpieces, number, price))