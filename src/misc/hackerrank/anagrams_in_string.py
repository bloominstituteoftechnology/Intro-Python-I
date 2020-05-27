import math
import os
import random
import re
import sys


def anagrams_in_string(s):
    '''
     Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
     For example 'mom', the list of all anagrammatic pairs is [m,m], [mo, om].
     Anagrams = the letters of one string can be rearranged to form the other string.
     'abba' => [a,a], [b,b], [ab, ba], [abb, bba]
    '''

    # Get all substrings.
    subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    total = 0
    sorted_dict = {}
    for sub in subs:
        sorted_dict[sub] = sorted(sub)
    for i in range(len(subs)):
        for j in range(i + 1, len(subs)):
            if sorted_dict[subs[i]] == sorted_dict[subs[j]]:
                total += 1
    print(total)
    return total

    # Maybe, after getting a substring, sort it and put it in lookup dict
    #   Make an entry if it doesn't exist
    #   If not, increment
    # For each entry that has value 2, increment total of pairs.

    # For brute force, compare each substring with the other substrings to see if they are anagrams.
    #   To see if anagrams, sorted lists of letters would be equal. For one way.


# anagrams_in_string('abba')  # 4
# anagrams_in_string('ifailuhkqq')  # 3
# 10 <-- ['k', 'kk', 'kkk', 'kkkk', 'k', 'kk', 'kkk', 'k', 'kk', 'k']
# anagrams_in_string('kkkk')
# # 6 [k,k] + 3 [kk,kk] + 1 [kkk,kkk]
anagrams_in_string('cdcd')  # 5  <-- [c,c], [d,d], [cd,dc], [cd, cd], [dc, cd]


'''
# Version with answer dictionary:

    # Get all substrings.
    subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    # print(subs)
    total = 0
    sorted_dict = {}
    answer_dict = {}
    for sub in subs:
        sorted_dict[sub] = sorted(sub)
        answer_dict[sub] = []
    # print(sorted_dict)
    for i in range(len(subs)):
        for j in range(i + 1, len(subs)):
            if subs[j] in answer_dict[subs[i]]:
                total += 1

            elif sorted_dict[subs[i]] == sorted_dict[subs[j]]:
                total += 1
                answer_dict[subs[i]].append(subs[j])
    print(total)
    return total
'''

'''
# Version with dictionary of key/value sorted_substring : instances of it
    subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    subs_dict = {}
    for sub in subs:
        sub_list = sorted(sub)
        print(sub_list)
        sub_str = ''.join([str(elem) for elem in sub_list])
        print(sub_str)

        if sub_str in subs_dict:
            subs_dict[sub_str] += 1
        else:
            subs_dict[sub_str] = 1

    print(subs_dict)
    
    total = 0
    for item in subs_dict.items():
        if item[1] > 1:
            total += 1
    print(total)
    return total
'''
