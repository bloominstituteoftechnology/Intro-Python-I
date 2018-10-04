# Use open to open file "foo.txt" for reading
f = open('foo.txt', 'r')

# Print all the lines in the file
print(f.read())

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
o = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
o.write('Testing 0 \n')
o.write('Testing 1 \n')
o.write('Testing 2 \n')

# Close the file
o.close()