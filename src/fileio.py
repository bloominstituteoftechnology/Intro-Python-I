import io
# Use open to open file "foo.txt" for reading
with open('foo.txt', mode='r', newline = '\n') as file:
	lines = file.read()
# Print all the lines in the file
print(lines)
# Close the file
# the with keyword closes file after successful write

# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file