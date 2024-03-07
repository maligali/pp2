import time, math

number = int(input("Enter a number: "))
delay = int(input("Enter delay ms: "))
msdelay = delay/1000

time.sleep(msdelay)
print(f"Square root of {number} after {delay} miliseconds is {math.sqrt(number)}")