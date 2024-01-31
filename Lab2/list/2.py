#Access Items

mylist = ["juice", "cola", "sprite"]
print(mylist[1]) #cola

#Negative indexing
mylist = ["juice", "cola", "sprite"]
print(mylist[-1]) #sprite

#Range if indexes
mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
print(mylist[1:5]) #['cola', 'sprite', 'lemonade', 'tea']

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
print(mylist[:4]) #['juice', 'cola', 'sprite', 'lemonade']

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
print(mylist[3:]) #['lemonade', 'tea', 'coffee']

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
print(mylist[-5:-2]) #['cola', 'sprite', 'lemonade']

#Check if Item Exists
mylist = ["juice", "cola", "sprite"]
if "juice" in mylist:
    print("Yes, 'juice' is in the the list")