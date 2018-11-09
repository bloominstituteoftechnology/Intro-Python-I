# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')
# Print all the lines in the file
for line in file:
    print (line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
arch = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
three_lines = ['line1', 'line2', 'line3']
arch.writelines(three_lines)

# Close the file
arch.close
