#!/usr/bin/env python3

# Function that takes in a string and returns that string with every other word reversed
# Made this similar function in Swift and made an attempt to translate it into Python

# NOTES:
# - I still would like to know if I can have access to the index inline without having to make an index property
# - I think there's still a space at the end which I should get rid of


def reverse_every_other_word_in(given_text):
    list_text = given_text.split()
    mixed_string = ""
    wordIndex = 0
    
    for word in list_text:
        if wordIndex % 2 != 0:
            reversed = word[::-1]
            mixed_string += reversed + " "
        else:
            mixed_string += word + " "
            
        wordIndex = wordIndex + 1
            
    return mixed_string
    
    
print(reverse_every_other_word_in("Some crazy guy is trying to code something"))
print(reverse_every_other_word_in("Function that takes in a string and returns that string with every other word reversed"))

