# Use open to open file "foo.txt" for reading
foo = open('foo.txt', 'r')
# Print all the lines in the file
lines = foo.readlines()
for line in lines:
    print(line)
# Close the file
foo.close()

# Use open to open file "bar.txt" for writing
bar = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
bar.write('Line1\nLine2\nLine3\n')
# Close the file
bar.close()