"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

from leetcode
"""


def twoSum(nums, target):
    # Make an answer dict with the key being the num, the value being what the difference is between the target and the num
    # Then go thru arr and see its complement exists in dict. If so return that index of complement.
    answer_dict = {}
    answer_arr = []
    for num in nums:
        answer_dict[num] = target - num
    print(answer_dict)
    for count, num in enumerate(nums):
        if answer_dict[num] in answer_dict and (num != answer_dict[num] or nums.count(num) > 1):
            # print('found it: ' + str(answer_dict[num]))
            # answer_arr.append(nums.index(num))
            # print(count)
            answer_arr.append(count)
            if num != answer_dict[num]:
                answer_arr.append(nums.index(answer_dict[num]))
            else:
                # Find 2nd index of num
                answer_arr.append(nums.index(
                    num, 1 + nums.index(answer_dict[num])))
            print(answer_arr)
            return(answer_arr)


# twoSum([2, 7, 11, 15], 9)
twoSum([3, 2, 4], 6)  # [1,2]
twoSum([3, 3], 6)  # [0,1]
