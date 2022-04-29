"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6,]

# Output the second element: 4:
print(a[slice(1,2)])

# Output the second-to-last element: 9
print(a[slice((len(a)-2),(len(a)-1))])

# Output the last three elements in the array: [7, 9, 6]
print(a[slice((len(a)-3),len(a))])

# Output the two middle elements in the array: [1, 7]
def getMiddleTwo(array):
    if(len(array) == 0):
        return ("the array is empty")
    elif(len(array) == 1):
        return(array[0])
    elif(len(array) % 2 == 0):
        start = int((len(array)/2) - 1)
        end = (start+2)
        return array[slice(start,end)]
    else:
        start = int(((len(array)-1)/2)-1)
        end = start + 2
        return array[slice(start,end)]
print(getMiddleTwo(a))

#I tried to make these solutions generalized to an array of any length
# Output every element except the first one: [4, 1, 7, 9, 6]
print( a[slice( 1, len(a) )] )

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[slice(0,(len(a)-1))])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[slice(7,12)])