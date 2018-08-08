# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')
# Print all the lines in the file
for line in file:
  print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
for i in range(4):
  file.write(f'{i}\n')

# Close the file
file.close()