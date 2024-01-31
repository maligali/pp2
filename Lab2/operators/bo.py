#Bitwise Operators
x = 6
y = 3
#& 	AND	Sets each bit to 1 if both bits are 1	
print(x & y) #2

#|	OR	Sets each bit to 1 if one of two bits is 1	
print(x | y) #7

#^	XOR	Sets each bit to 1 if only one of two bits is 1	
print(x ^ y) #5

#~	NOT	- Inverts all the bits	
print(~x) #-7

#<<	Zero fill left shift -	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
print(x << 2) #24

#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(x >> 2) #1