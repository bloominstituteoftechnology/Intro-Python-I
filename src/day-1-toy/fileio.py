# Use open to open file "foo.txt" for reading
f = open("foo.txt", 'r')
# Print all the lines in the file
for line in f:
    print(line)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
barFile = open("bar.txt", 'w')
# Use the write() method to write three lines to the file
barFile.write('This is a sentence\n I am another sentence\n Goodbye')
# Close the file
barFile.close()