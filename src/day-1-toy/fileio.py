# Use open to open file "foo.txt" for reading
f = open('foo.txt', 'r')

# Print all the lines in the file
print(f.read())

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
o = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
o.write('Line 1 \n')
o.write('Line 2 \n')
o.write('Line 3 \n')

# Close the file
f.close()