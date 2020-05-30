"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef"
"""
import re


class Solution:
    def decodeString(self, s: str) -> str:
        # There's probably an awesome regex way to do this
        # Until I can figure it out, try a less-awesome way.
        # Loop through string
        # If num, store as var current_num
        # If starting bracket, set flag to true
        # If letter and flag is true, store letter in var current_string
        # If letter and flag is false, add letter to return_string
        # If closing bracket,
        #   add current_string to return_string, current_num times
        #   reset current_string and current_num and flag

        return_string = ''
        in_brackets = False
        current_num = 0
        inner_current_num = 0
        current_string = ''
        inner_current_string = ''

        for i, char in enumerate(s):
            if char.isdigit() and not current_num:
                current_num = int(char)
            elif char.isdigit() and current_num:
                if s[i-1].isdigit():
                    current_num = int(str(current_num) + char)
                else:
                    inner_current_num = int(char)
            elif char == '[' and not in_brackets:
                in_brackets = True
            elif char == '[' and in_brackets:
                # print("in nested now")
                continue
            elif in_brackets and inner_current_num and char != ']':
                # print("putting char in inner_string")
                inner_current_string += char
                # print(inner_current_string)
            elif in_brackets and char != ']':
                current_string += char

            elif not in_brackets and char != ']':
                return_string += char
                current_string = ''
            elif char == ']' and inner_current_string:
                # print("Adding inner string to current_string")
                # print(current_string)
                current_string += (inner_current_string * inner_current_num)
                # print(current_string)
                inner_current_string = ''
                inner_current_num = 0
            elif char == ']' and not inner_current_string:
                # print("in last condition")
                # print(current_string)
                # print(current_num)
                return_string += (current_string * current_num)
                current_string = ''
                current_num = 0
                in_brackets = False

        print(return_string)
        return(return_string)


s = Solution()
s.decodeString("3[a]2[bc]")  # "aaabcbc"
s.decodeString("3[a2[c]]")  # "accaccacc"
s.decodeString("2[abc]3[cd]ef")  # "abcabccdcdcdef"
# s.decodeString("100[leetcode]")
# "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
# 3[z] +
# 2 [2[y]pq4[2[jk]e1[f]]] + ef
#  broken down 2[y] + pq + 4[[2[jk]e1[f]]]
#                            2[jk] + e + 1[f]

# "zzz
#   yypq jkjk ef jkjk ef jkjk ef jkjkef
#   yypq jkjk ef jkjk ef jkjk ef jkjkef    ef"

# test = 3 * ('z') + 2 * ((2 * 'y') + 'pq' +
#                        4*(2*('jk') + 'e' + 1*('f'))) + 'ef'
# print(test)
