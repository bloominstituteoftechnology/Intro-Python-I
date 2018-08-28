# Use open to open file "foo.txt" for reading
f = open('/Users/michaelreal/Documents/GitHub/Intro-Python/src/day-1-toy/foo.txt')
# Print all the lines in the file
lines = f.read()
print(lines)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('/Users/michaelreal/Documents/GitHub/Intro-Python/src/day-1-toy', "w")
# Use the write() method to write three lines to the file
f.write('Line 1\n')
f.write('Line 2\n')
f.write('Line 3')
# Close the file
f.close()