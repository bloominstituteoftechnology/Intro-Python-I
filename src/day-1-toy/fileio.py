# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')
# Print all the lines in the file
print(file.read())

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
f.write('a line of text \n')
f.write('another line of text \n')
f.write('a third line \n')
# Close the file
f.close()