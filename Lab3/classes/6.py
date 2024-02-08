import math
def isPrime(n):
    if n < 2:
        return False
    else: 
        for i in range(2, int(math.sqrt(n)) + 1):
           if n % i == 0:
              return False
        return True

def filter_prime(numbers):
    prf = filter(lambda n : isPrime(n), numbers)
    return list(prf)

print(filter_prime([1, 4, 13, 66, 37, 23, 11]))