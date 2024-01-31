thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
print(thisdict)

#Dictionary Items
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
print(thisdict["name"])

#Duplicate values will overwrite existing values:
thisdict = {
  "name" : "Malik",
  "name" : "Malika",
  "age" : 17,
  "gender" : "Male",
  "gender" : "Female"
}
print(thisdict)

#String, int, boolean, and list data types:

thisdict = {
  "brand": "BMW",
  "electric": True,
  "year": 2014,
  "colors": ["dark red", "black"]
}

thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
print(type(thisdict))

thisdict = dict(name = "Malika", age = 17, country = "Kazakhstan")
print(thisdict)