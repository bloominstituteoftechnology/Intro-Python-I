'''
https://slack-redir.net/link?url=https%3A%2F%2Fleetcode.com%2Fproblems%2Ffind-the-duplicate-number%2F

Given an array nums containing n + 1 integers where each integer 
is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Input: [1,3,4,2,2]
Output: 2

Input: [3,1,3,4,2]
Output: 3

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class Solution:
    def findDuplicate(self, nums):
        # First idea is to make a visited set.
        # Loop through nums
        # If num in visited:
        #   return num
        # Else, add to visited set.
        # Will this satisfy the requirements?

        visited = set()
        for num in nums:
            if num in visited:
                return num
            else:
                visited.add(num)


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
