"""
Classes and Objects
"""
# encapsulate variables and functions into one entity
# classes are templates to create objects

# # 1. basic class
class MyClass:
     variable = "what is up?"

     def function(self):
         print("This is a message from inside the class.")

# # 2. assign instance to object
class MyClass:
     variable = "what is up?"

     def function(self):
         print("This is a message from inside the class.")


my_first_object = MyClass()

# # 3. accessing object variables
class MyClass:
         variable = "what is up?"

         def function(self):
            print("This is a message from inside the class.")


my_first_object = MyClass()

print(my_first_object.variable)

# # 4. multiple instances
class MyClass:
     variable = "what is up?"

     def function(self):
         print("This is a message from inside the class.")


my_first_object = MyClass()
my_second_object = MyClass()

my_second_object.variable = "nothing much."

# # Then print out both values
print(my_first_object.variable)
print(my_second_object.variable)

# # 5. accessing object functions
class MyClass:
    variable = "what is up?"

     def function(self):
         print("This is a message from inside the class.")


my_first_object = MyClass()

my_first_object.function()
