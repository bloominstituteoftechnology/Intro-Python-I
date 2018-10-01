# Use open to open file "foo.txt" for reading
foo = open('foo.txt', 'r')
# Print all the lines in the file
lines = foo.read()
print(lines)
# Close the file
foo.close()

# Use open to open file "bar.txt" for writing
bar = open('bar.txt', 'w+')
# Use the write() method to write three lines to the file
bar.write('Line 1\n')
bar.write('Line 2\n')
bar.write('Line 3\n')
# Close the file
bar.close()