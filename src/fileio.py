# Use open to open file "foo.txt" for reading
file = open('./src/foo.txt', 'r')
# Print all the lines in the file
for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('./src/bar.txt', 'w')

# Use the write() method to write three lines to the file
file.write('first line\n')
file.write('second line\n')
file.write('third line\n')

# Close the file
file.close()
