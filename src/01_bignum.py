# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

#print(2**65536)


# x = [2, 3, 5, 6, 7, 1, 3]

# # multiplied = [i * 2 for i in x]
# # print(multiplied)
# import pandas as pd 
# x = [2, 3, 5, 6, 7, 1, 3]
# # multiplied = []
# # for i in x:
# #     multiplied.append(i / 2)
# # print(multiplied)

# # s = pd.Series(x)
# # s * 2

# big_numbers = [num * 20 for num in x ]
# print(big_numbers)



# squares = 65536

# result = list(map(lambda x: 2 ** x, range(65536)))

# for i in range(squares):
#     print('2 raised to the power of', i, 'is', result[i])

square = [num ** 2 for num in range(65536) ]
print(square)