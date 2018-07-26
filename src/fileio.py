# Use open to open file "foo.txt" for reading
with open('foo.txt', mode='r', newline = '\n') as file:
	lines = file.read()
# Print all the lines in the file
print(lines)
# Close the file
# the with keyword closes file after successful write

text1 = 'first line'
text2 = 'second line'
text3 = 'third line'

# Use open to open file "bar.txt" for writing
with open('bar.txt', mode='w', newline='\n') as file:
	# Use the write() method to write three lines to the file
	file.write("{0}\n".format(text1))
	file.write("{0}\n".format(text2))
	file.write("{0}\n".format(text3))

# Close the file