#List Comprehension

drinks = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
mylist = []
for x in drinks:
    if "a" in x:
        mylist.append(x)
print(mylist)


mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = [x for x in mylist if "a" in x]
print (newlist)

'''The Syntax
newlist = [expression for item in iterable if condition == True]'''

#condition

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = [x for x in mylist if x != "cola"]
print(newlist)

#with no if statement
mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = [x for x in mylist]
print(newlist)

#Iterable
newlist = [x for x in range(13)]
print (newlist)

newlist = [x for x in range(7) if x < 3]
print (newlist)

#Expression
mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = [x.upper() for x in mylist]
print(newlist)

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = ['goodbye' for x in mylist]
print(newlist)

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = [x if x != "cola" else "pepsi" for x in mylist]
print(newlist)