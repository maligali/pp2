#Remove item

set1 = {"cat", "dog", "rabbit"}
set1.remove("dog")
print(set1)

set1 = {"cat", "dog", "rabbit"}
set1.discard("dog")
print(set1)

set1 = {"cat", "dog", "rabbit"}
x = set1.pop()
print(x)
print(set1)

set1 = {"cat", "dog", "rabbit"}
set1.clear()
print(set1)

set1 = {"cat", "dog", "rabbit"}
#del set1 //name 'set1' is not defined
print(set1)