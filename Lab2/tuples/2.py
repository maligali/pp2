#Access tuple items
notmytuple = ("juice", "cola", "sprite")
print(notmytuple[2])

notmytuple = ("juice", "cola", "sprite")
print(notmytuple[-3])

notmytuple = ("juice", "cola", "sprite", "water", "lemonade", "kvas", "milkshake")
print(notmytuple[3:6])

notmytuple = ("juice", "cola", "sprite", "water", "lemonade", "kvas", "milkshake")
print(notmytuple[:5])

notmytuple = ("juice", "cola", "sprite", "water", "lemonade", "kvas", "milkshake")
print(notmytuple[3:])

#Range of Negative Indexes

notmytuple = ("juice", "cola", "sprite", "water", "lemonade", "kvas", "milkshake")
print(notmytuple[-5:-3])

notmytuple = ("juice", "cola", "sprite", "water", "lemonade", "kvas", "milkshake")
if "kvas" in notmytuple:
    print("Yes, 'kvas' is in the drinks tuple")