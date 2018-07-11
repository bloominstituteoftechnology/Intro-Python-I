# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

#x = input("Enter comma-separated numbers: ").split(',')
x = input("testing")
print(type(x))

x = x.split(",")
print(x)
evenElement = []
for i,val in enumerate(x): 
  if i % 2 == 0:
    evenElement.append(val)
# What do you need between the square brackets to make it work?
print("even",evenElement)
y = [*evenElement]

print(y)

