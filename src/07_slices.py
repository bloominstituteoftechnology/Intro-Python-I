"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

# Output the second element: 4:
def sec_elem(a):

    print(a[1])

# Output the second-to-last element: 9
def sec_last_elem(a):

    print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
def last_three_elem(a):

    print(a[-3:])

# Output the two middle elements in the array: [1, 7]
def two_middle_elem(a):

    print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
def all_but_first_elem(a):

    print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
def all_but_last_elem(a):

    print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
def output_world(a):

    print(s[7:12])

if __name__ == "__main__":
    a = [2, 4, 1, 7, 9, 6]

    sec_elem(a)
    sec_last_elem(a)
    last_three_elem(a)
    two_middle_elem(a)
    all_but_first_elem(a)
    all_but_last_elem(a)
    output_world(a)