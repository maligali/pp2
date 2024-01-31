#Remove items

thisdict = {
  "name" : "Kate",
  "age" : 42,
  "gender" : "Female"
}
thisdict.pop("gender")
print(thisdict)

thisdic = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
thisdic.popitem()
print(thisdic)

thisdic = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
del thisdic["age"]
print(thisdic)

thisdic = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
thisdic.clear()
print(thisdic)