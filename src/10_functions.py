# # Write a function is_even that will return true if the passed-in number is even.

# # YOUR CODE HERE


# # def is_even(num):
# #     if num % 2 == 0:
# #         return True
# #     else:
# #         return False


# # Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)
# print(num % 2 == 0)
# # Print out "Even!" if the number is even. Otherwise print "Odd"

# # YOUR CODE HERE


def double_list(li):
    for i in range(0, len(li)):
        li[i] *= 2


num_list = [1, 2, 3, 4, 5]
double_list(num_list)
print(num_list)
