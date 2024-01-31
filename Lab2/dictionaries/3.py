#Change values
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
thisdict["age"] = 18
print(thisdict)

thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
thisdict.update({"age": 18})
print(thisdict)