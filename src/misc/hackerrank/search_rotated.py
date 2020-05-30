'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
# Index of array needs to be returned, so I probably don't want to change the order.
import math


class Solution:
    def search(self, nums, target):
        # if target is greater than max value, return -1
        '''
        max_value = max(nums)
        # print(max_value)
        if target > max_value:
            return -1
        min_value = min(nums)
        if target < min_value:
            return -1
        '''
        if len(nums) < 1:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if target == nums[0]:
            return 0

        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high)//2
            print('middle: ' + str(middle))
            if target == nums[middle]:
                return middle
            # ([1, 2, 3, 4, 5, 6], 2))
            elif target <= nums[-1] and target < nums[middle]:
                low = middle + 1
                if low < len(nums) and nums[low] == target:
                    return low
            elif target < nums[middle]:
                high = middle - 1
            elif target > nums[middle]:
                low = middle + 1
        return -1


s = Solution()
'''
print(s.search([4, 5, 6, 7, 0, 1, 2], 4))
print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
print(s.search([4, 5, 6, 7, 0, 1, 2], 6))
print(s.search([4, 5, 6, 7, 0, 1, 2], 7))
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 1))
print(s.search([4, 5, 6, 7, 0, 1, 2], 2))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
print(s.search([1, 3], 0))
print(s.search([1, 3], 1))
print(s.search([1, 3], 3))
print(s.search([1, 3, 5], 1))
print('\n')

print(s.search([1, 2, 3, 4, 5, 6], 1))
'''
print(s.search([1, 2, 3, 4, 5, 6], 2))
'''
print(s.search([1, 2, 3, 4, 5, 6], 3))
print(s.search([1, 2, 3, 4, 5, 6], 4))
print(s.search([1, 2, 3, 4, 5, 6], 5))
print(s.search([1, 2, 3, 4, 5, 6], 6))
'''
# Old Idea Graveyard
'''
# I guess I could look at a middle pointer's neighbors
#  If the one to the right is smaller and target is smaller, go that way. Etc.
    # print(nums)
    # print(target)
    middle = len(nums) // 2
    print(nums[middle])
    while nums[middle] != target:
        if nums[middle - 1] < nums[middle]:
            if target < nums[middle]:
                middle = len(nums[:middle]) // 2
                print(nums[middle])
            else:
                middle = len(nums[middle:]) + (len(nums[middle:]) // 2)
                print(nums[middle])
        if nums[middle - 1] > nums[middle]:
            if target < nums[middle]:
                middle = len(nums[middle:]) + (len(nums[middle:]) // 2)
                print(nums[middle])
            else:
                middle = len(nums[:middle]) // 2
                print(nums[middle])
    return nums[middle]
    '''

'''
    # find pivot
        pivot = 0
        for i in range(len(nums) - 1):
            print(i)
            if nums[i+1] < nums[i]:  # [4,5,6,7,0,1,2]
                print("found pivot")
                print(i)
                pivot = i
                break
        print('next')
        new_nums = nums[pivot + 1:] + nums[:pivot]
        print('new nums: ' + str(new_nums))
    '''

'''
    # O(n)
    for i, num in enumerate(nums):
            if num == target:
                return i
    '''
'''
        middle = len(nums) // 2
        is_found = False
        while not is_found:
            if nums[middle] == target:
                is_found = True
                # print(middle)
                return middle
            elif nums[middle] < target or target < nums[-1]:
                # print('NEW middle: ' + str(middle))
                # middle = middle + math.ceil(middle/2)
                middle += middle//2
                if middle == 1:
                    middle = 2
            else:
                middle = middle//2
                # print('new middle: ' + str(middle))
        '''
