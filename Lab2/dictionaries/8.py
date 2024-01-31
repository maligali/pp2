mypets = {
  "cat1" : {
    "name" : "Kit",
    "year" : 2024
  },
  "cat2" : {
    "name" : "Tigra",
    "year" : 2013
  },
  "dog3" : {
    "name" : "Druzhok",
    "year" : 2021
  }
}

print(mypets["cat2"]["name"])

cat1 = {
    "name" : "Kit",
    "year" : 2024
  }
cat2 = {
    "name" : "Tigra",
    "year" : 2013
  },
dog3 = {
    "name" : "Druzhok",
    "year" : 2021
  }

mypets = {
    "cat1" : cat1,
    "cat2" : cat2,
    "dog3" : dog3
}

print(mypets["dog3"]["year"])