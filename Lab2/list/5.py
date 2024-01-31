#Remove list items

mylist = ["juice", "cola", "sprite"]
mylist.remove("juice")
print(mylist)

mylist = ["juice", "cola", "sprite", "juice", "water"]
mylist.remove("juice")
print(mylist)

#Remove specified index
mylist = ["juice", "cola", "sprite"]
mylist.pop(2)
print(mylist)

mylist = ["juice", "cola", "sprite"]
mylist.pop()
print(mylist)

mylist = ["juice", "cola", "sprite"]
del mylist[1]
print(mylist)

mylist = ["juice", "cola", "sprite"]
del mylist
print(mylist) #deletes the entire list

mylist = ["juice", "cola", "sprite"]
mylist.clear()
print(mylist)