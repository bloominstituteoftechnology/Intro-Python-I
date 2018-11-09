# Use open to open file "foo.txt" for reading
f = open('foo.txt', 'r')
# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w')

# Use the write() method to write three lines to the file

f.write('line 1 \n')
f.write('line 1 \n')
f.write('line 1 \n')

# Close the file
f.close()