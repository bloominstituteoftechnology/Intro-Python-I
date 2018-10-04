# Use open to open file "foo.txt" for reading
with open('foo.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Print all the lines in the file
# Close the file


# Use open to open file "bar.txt" for writing
with open('bar.txt', 'w') as f:
    f.write('This is a test\n')
    f.write('Only a test\n')
    f.write('Please do not panic\n')

# Use the write() method to write three lines to the file

# Close the file
