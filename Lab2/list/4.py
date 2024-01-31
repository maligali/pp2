#Add list items
mylist = ["juice", "cola", "sprite"]
mylist.append("DaDa")
print(mylist)

mylist = ["juice", "cola", "sprite"]
mylist.insert(1, "DaDa")
print(mylist)

mylist = ["juice", "cola", "sprite"]
newlist = ["tea", "coffee", "hot chocolate"]
mylist.extend(newlist)
print(mylist)

mylist = ["juice", "cola", "sprite"]
mytuple = ("tea", "coffee")
mylist.extend(mytuple)
print(mylist)