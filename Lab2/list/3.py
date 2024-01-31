#Change item value

mylist = ["juice", "cola", "sprite"]
mylist[1] = "fanta"
print(mylist) #['juice', 'fanta', 'sprite']

#Change a Range of Item Values

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
mylist[2:4] = ["fanta", "mirinda"]
print(mylist) #['juice', 'cola', 'fanta', 'mirinda', 'tea', 'coffee']

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
mylist[1:2] = ["fanta", "mirinda"]
print(mylist) #['juice', 'fanta', 'mirinda', 'sprite', 'lemonade', 'tea', 'coffee']     

mylist = ["juice", "cola", "sprite"]
mylist[1:3] = ["fanta"]
print(mylist) #['juice', 'fanta']

mylist = ["juice", "cola", "sprite"]
mylist.insert(1, "fanta")
print(mylist) #['juice', 'fanta', 'cola', 'sprite']  