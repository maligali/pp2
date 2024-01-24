'''
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType'''

x = 8
print(type(x))

x = "Good"	#str	
x = 17	#int	
x = 17.5	#float	
x = 1j	#complex	
x = ["a", "b", "c"]	#list	
x = ("a", "b", "c")	#tuple	
x = range(6)	#range	
x = {"name" : "Kate", "gender" : "F"}	#dict	
x = {"a", "b", "c"}	#set	
x = frozenset({"a", "b", "c"})	#frozenset	
x = False	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#Setting Data Type Examples
x = str("I am happy!") #str
x = int(18) #int
x = range(8) #range