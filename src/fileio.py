# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'rU')

# Print all the lines in the file
for line in file:
  print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
file.write('Turns out that I really like Python.')

# Close the file
file.close()