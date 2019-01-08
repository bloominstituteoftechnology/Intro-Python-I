# Write a method that takes one argument, a positive integer, and returns a
# list of digits in the number.

# Input: positive integer
# Output: digits of the input integer

# Example:
# Input: 12345
# Output: [1, 2, 3, 4, 5]

# Input: 7
# Output: [7]

# Input: 444
# Input: [4, 4, 4]

# Pseudocode
# START
# Given a positive integer called num
# Create an empty list called digits
# While num is greater than 0
#   - Get the remainder of num / 10
#   - Prepend remainder to digits
#   - Get rid of the last digit of num by dividing it by 10
#   - Note: result should be int
# Return digits
# END

# Solution 1
def digit_list(num):
    digits = []

    while num > 0:
        remainder = num % 10
        digits = [remainder] + digits
        num = num // 10

    return digits


# Solution 1.5
def digit_list(num):
    digits = []

    while num > 0:
        remainder = num % 10
        digits.insert(0, remainder)
        num = num // 10

    return digits


print(digit_list(12345))  # [1, 2, 3, 4, 5]
print(digit_list(7))  # [7]
print(digit_list(444))  # [4, 4, 4]

# Solution 2: Converting int to str
def digit_list1(num):
    # Convert num to str
    num_str = str(num)
    # Iterate through and convert back to int each char in num_str
    # Prepend each digit to digits
    digits = [int(n) for n in num_str]
    return digits


print(digit_list1(12345))  # [1, 2, 3, 4, 5]
print(digit_list1(7))  # [7]
print(digit_list1(444))  # [4, 4, 4]
