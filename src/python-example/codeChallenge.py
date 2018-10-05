# 3. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # Your code here
  letter = s[0]
  string = s[1:]
  ss = string.replace(letter, '*' )
  return letter + ss
  pass

print(fix_start('babble'))