# Write a function that takes an array of strings and return the longest string in the array.
# const strings1 = ['short', 'really, really long!', 'medium'];
#   console.log(longestString(strings1)); // <--- 'really, really long!'
# Edge case: If you had an array which had two "longest" strings of equal length, your function should just return the first one.
# const strings2 = ['short', 'first long string!!', 'medium', 'abcdefghijklmnopqr'];
#   console.log(longestString(strings2)); // <--- 'first long string!'

def longest_string(list):
    count = 0
    for item in list:
        if (len(item) > count):
            count = len(item)
            word = item
    return word

strings1 = ['short', 'really, really long!', 'medium']
print(longest_string(strings1))

strings2 = ['short', 'first long string!!', 'medium', 'abcdefghijklmnopqr']
print(longest_string(strings2))
