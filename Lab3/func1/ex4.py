#4
import math
def prime(n):
  if n < 2:
    return False
  else: 
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
  return True

def filter_prime(num):
  list = [n for n in num if prime(n)]
  return list
print(filter_prime([41, 39, 55, 3, 11])) 