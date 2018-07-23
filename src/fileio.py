# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'rU')

# Print all the lines in the file
for line in file:
  print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file