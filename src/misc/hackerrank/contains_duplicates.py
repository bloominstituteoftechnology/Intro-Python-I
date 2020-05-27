"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

[1,2,3,1] -> true
[1,2,3,4] -> false
[1,1,1,3,3,4,3,2,4,2] -> true
from leetcode
"""


def containsDuplicate(arr):
    contains_duplicates = False
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for value in count_dict.values():
        if value > 1:
            contains_duplicates = True
            # print("True")
            return True
    # print("False")
    return False


# containsDuplicate([1, 2, 3, 1])
# containsDuplicate([1, 2, 3, 4])
# containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
