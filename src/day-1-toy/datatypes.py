x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
print(x + int(y))

# Write a print statement that combines x + y into the string value 57
print(str(x) + y)

type(x)       # <class 'int'>
type(y)       # <class 'str'>
type(int(y))  # <class 'int'>
type(str(x))  # <class 'str'>

int("8", 10)    # any data type with its base
int("01000", 2) # 8
float(8)        # 8.0
ord()           # converts a character to unicode number
hex()           # converts an int to hexadecimal str
oct()           # converts an int to octal str
tuple()         # converts to a tuple
tuple([1,])     # (1,)
tuple("123")    # ("1", "2", "3")
set()           # converts to a set
set([1,2,1,2])  # {1, 2}
list()          # converts to a list
list("123")     # ["1", "2", "3"]
list({"1":"a","2":"b"}) # ["1", "2"]
dict()          # convert a tuple (key,value) into a dictionary
str()           # convert an int to a str
complex(real,imag) # converts a real number to an imaginary number denoted by "j"