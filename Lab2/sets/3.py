#Add Set Items

#add items
set1 = {"cat", "dog", "rabbit"}
set1.add("hamster")
print(set1)

#add sets
dom = {"cat", "dog", "rabbit"}
nedom = {"horse", "pig", "cow"}
dom.update(nedom)
print(dom)

#add any iterable
dom = {"cat", "dog", "rabbit"}
mylist = ["rat", "spider"]
dom.update(mylist)
print(dom)