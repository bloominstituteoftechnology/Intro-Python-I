import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    '''
    Given two strings, determine if they share a common substring. 
    A substring may be as small as one character.

    For example, the words "a", "and", "art" share the common substring a. 
    The words "be" and "cat" do not share a substring.

    It should return a string, either YES or NO based on whether the strings share a common substring
    '''
    # Turn s1 chars into a set
    # Turn s2 chars into a set
    # See if set1.isdisjoint(set2) which returns True if none of the items are present in both sets.
    set1 = set(s1)
    set2 = set(s2)
    result = not set1.isdisjoint(set2)
    if result == True:
        # print('YES')
        return 'YES'
    else:
        # print('NO')
        return 'NO'


twoStrings('cat', 'can')
