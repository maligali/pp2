#Sort lists

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
mylist.sort()
print(mylist) #alphabetical sorting

mylist = [484, 33, 68, 99, 21]
mylist.sort()
print(mylist) #numerically

#Sort descending
mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
mylist.sort(reverse = True)
print(mylist)

mylist = [484, 33, 68, 99, 21]
mylist.sort(reverse = True)
print(mylist)

#Customize Sort Function
def func(x):
    return abs(x - 22)
mylist = [484, -33, 68, 99, -21]
mylist.sort(key = func)
print(mylist)

#Case Insensitive Sort
mylist = ["dog", "rabbit", "Cat", "Hamster", "rat"]
mylist.sort()
print(mylist)

mylist = ["cat", "Rabbit", "dog", "hamster", "Rat"]
mylist.sort(key = str.lower)
print(mylist)

#Reverse Order
mylist = ["dog", "rabbit", "Cat", "Hamster", "rat"]
mylist.reverse()
print(mylist)


#Copy List
mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = mylist.copy()
print(newlist)

mylist = ["juice", "cola", "sprite", "lemonade", "tea", "coffee"]
newlist = list(mylist)
print(newlist)

#Join list
list1 = ["x", "y", "z"]
list2 = [7, 8, 9]
list3 = list1 + list2
print(list3)

list1 = ["x", "y", "z"]
list2 = [7, 8, 9]
for x in list2:
    list1.append(x)
print(list1)

list1 = ["x", "y", "z"]
list2 = [7, 8, 9]
list1.extend(list2)
print(list1)

#List methods
'''()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''