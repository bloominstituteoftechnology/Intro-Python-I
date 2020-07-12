# Create list
l = []
print(l)

# Create list with numbers
num_list = [1, 2, 3, 4]
print(num_list)

# Add element to empty list
l.append(77)
print(l)

# Print all values in num_list
for element in num_list:
    print(element)

# Print all values in l
for element in l:
    print(element)

# If you want the index of the element, use enumerate to access

for(i, elem) in enumerate(num_list):
    print(f'Element {i} is {elem}')


# How you loop through a certain number of times
for x in range(10):
    print(x)