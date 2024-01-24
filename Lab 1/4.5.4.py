x = "hard"

def myfunc():
  global x
  x = "complex"

myfunc()

print("Math is " + x)