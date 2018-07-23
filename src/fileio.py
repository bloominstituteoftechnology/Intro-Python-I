# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')

text = file.read();
print(text)

# Print all the lines in the file

# Close the file
file.close()


# Use open to open file "bar.txt" for writing

file = open('bar.txt', 'w')
file.write('line1\nline2\nline3\n')
file.close()
# Use the write() method to write three lines to the file

# Close the file
