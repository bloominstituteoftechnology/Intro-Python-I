# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")

# Print all the lines in the file
print(file.read())

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")

# Use the write() method to write three lines to the file

newLines = ['line1 \n', 'line2 \n', 'line3 \n']
for line in newLines:
        file.write(line)

# Close the file
file.close()
