#Loop lists
mylist = ["juice", "cola", "sprite"]
for x in mylist:
    print(x)

#Loop Through the Index Numbers
mylist = ["juice", "cola", "sprite"]
for i in range(len(mylist)):
    print(mylist[i])

#using a while loop
mylist = ["juice", "cola", "sprite"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

#Looping Using List Comprehension
mylist = ["juice", "cola", "sprite"]
[print(x) for x in mylist]

