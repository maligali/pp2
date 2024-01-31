notmytuple = ("juice", "cola", "sprite")
print(notmytuple)

notmytuple = ("juice", "cola", "sprite", "cola", "juice")
print(notmytuple) #allows duplicates

notmytuple = ("juice", "cola", "sprite")
print(len(notmytuple))

notmytuple = ("juice",)
print(type(notmytuple)) #typle

notmytuple = ("juice")
print(type(notmytuple)) #str

#Data Types
t1 = ("apple juice", "water", "cola") #string
print(t1)
t2 = (33, 22 , 11, 99) #int
print(t2)
t3 = (False, False, False) #boolean
print(t3)

#A tuple can contain different data types:

tuple = (33, False, "aaa", 33.4)
print(tuple)

notmytuple = ("juice", "cola", "sprite")
print(type(notmytuple)) #<class 'tuple'>

notmytuple = tuple(("juice", "cola", "sprite")) #does not work on VScode
print(notmytuple) 