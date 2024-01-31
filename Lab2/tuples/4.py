#Unpacking a Tuple
tup = ("juice", "cola", "sprite")

(orange, brown, white) = tup

print(orange)
print(brown)
print(white)

#Using Asterisk
tup = ("juice", "cola", "sprite", "fanta")

(orange, brown, *white) = tup

print(orange)
print(brown)
print(white)

tup = ("juice", "cola", "sprite", "tea", "water")

(orange, *clear, white) = tup

print(orange)
print(clear)
print(white)