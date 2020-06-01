"""
Tuples
"""
# A tuple is a collection which is ordered and unchangeable


# # 1. In Python, tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# # 2. accessing
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# # 3. reverse indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# # 4. slicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# # 5. negative slicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# # 6. iterating
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# # 7. contains?
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
   print("Yes, 'apple' is in the fruits tuple")

# # 8. creating a tuple with one item
thistuple = ("apple",)
print(type(thistuple))

# #NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# # 9. concatenating tuples with addition operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)