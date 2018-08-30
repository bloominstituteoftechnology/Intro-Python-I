# Use open to open file "foo.txt" for reading
filename = './foo.txt'
fh = open(filename, 'r')
# Print all the lines in the file
print(fh.read())
# Close the file
fh.close()

# Use open to open file "bar.txt" for writing
bar = open('./bar.txt', 'w')
# Use the write() method to write three lines to the file
bar.write('line 1')
bar.write('line 2')
bar.write('line 3')
# Close the file
bar.close()