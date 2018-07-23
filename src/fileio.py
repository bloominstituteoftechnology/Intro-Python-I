import os

# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
for line in file.readlines():
    print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
anotherFile = open("bar.txt", mode="w")

# Use the write() method to write three lines to the file
anotherFile.writelines("Hey,\n How's it going?,\n Fine")

# Close the file
anotherFile.close()