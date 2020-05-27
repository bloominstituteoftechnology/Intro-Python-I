"""
You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make s=ABAB in 2 deletions.
"""
import math
import os
import random
import re
import sys


def alternatingCharacters(s):
    # Use regex replace to replace any repeating chars with a single char.

    # re.sub takes 3 args: the regex pattern, a new string, and the string to be processed,
    # with an opt 4th arg as the max num of replacments

    # Note: re.subn() was promising because returns a tuple with the 2nd value being the number of parts replaced
    # But doesn't work for this specific problem because clusters are treated as single parts.

    new_s = re.sub(r'(.)\1+', r'\1', s)
    # print(new_s)

    # Subtract the length of the resulting string from the length of the original string and return that num.
    # print(len(s) - len(new_s))
    return(len(s) - len(new_s))


# alternatingCharacters('AAAA')  # 3
# alternatingCharacters('BBBBB')  # 4
# alternatingCharacters('ABABABAB')  # 0
# alternatingCharacters('BABABA')  # 0
# alternatingCharacters('AAABBB')  # 4
