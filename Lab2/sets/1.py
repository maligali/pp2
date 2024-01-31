#Python sets
set1 = {"cat", "dog", "rabbit"}
print(set1)

#Duplicates not allowed and are going to be ignored:
set1 = {"cat", "dog", "rabbit", "dog"}
print(set1)

#True and 1 is considered the same value
set1 = {"cat", "dog", "rabbit", True, 1}
print(set1)

#Get the Length of a Set
set1 = {"cat", "dog", "rabbit"}
print(len(set1))

set1 = {"alma", "banan", "vishnya"} #str
print(set1)
set2 = {5, 3, 8, 11, 2} #int
print(set2)
set3 = {False, False, False} #boolean
print(set3)

set1 = {"xyz", 34.35, False, 4022} #diff data types
print(set1)

set1 = {"cat", "dog", "rabbit"}
print(type(set1))

set1 = set(("cat", "dog", "rabbit"))
print(set1)