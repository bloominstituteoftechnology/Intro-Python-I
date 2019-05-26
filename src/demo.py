# # name = "Rob"
# # print("Yo, my name is " + name)

# # newName = 'Destiny'
# # age = 21
# # print("My name is {} and I am {} years old" .format(newName, age))

# # profile = {'name': "Kyle", 'age': 32}
# # print("My name is {name} and I am {age} years old".format(**profile))


# # def lower_case(input):
# #     return input.lower()

# # name = "Derek"
# # age = 41
# # print(f"{lower_case(name)} is {age} years old")
# # name = "SEAN"
# # print(f"{name.lower()}")
# #once printed, does the following code no longer have access to previous variables(or whatev3er they are called)?


# m = [1, 2, 3]
# m.append([4, 5])
# m.clear()
# n = [1, 2, 3]
# n.extend([4, 5])
# n.insert(0,-1)
# # n.remove(-1)
# q = n.count(3)
# # o = n.pop(0)
# # p = n.index(2)
# a = n.copy()
# r = n.sort(reverse = True)
# s = sorted(n, reverse = True)

# # print(m)
# print(a)
# # print(n)
# # print(o)
# # print(p)
# # print(q)
# # print(r)
# # print(s)

# # for num in a:
# #     print(num)
# for i in range(0, len(a)):
#     print("The value at index " + str(i) + " is " + str(a[i]))

# numbers = [6, 7, 8, 9, 10]
# # evens = []
# also_evens = [num for num in numbers if num % 2 == 0]
# squares = []
# squares_too = [num * num for num in numbers]

# for num in numbers:
#     squares.append(num * num)

# # for num in numbers:
# #     if num % 2 == 0:
# #         evens.append(num)


# # print(evens)
# print(also_evens)
# print(squares)
# print(squares_too)

# names = ["andrew", "Garret", "Alex", "ariel", "Destiny", "Amber", "Trevor"]

# as_only = [name.capitalize() for name in names if name[0] == "A" or name[0] == "a"]

# print(as_only)


