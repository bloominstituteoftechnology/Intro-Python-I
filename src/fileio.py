# Use open to open file "foo.txt" for reading
newFile = open("foo.txt", "r")
# Print all the lines in the file
for line in newFile:
    print(line)

# Close the file
newFile.close()

# Use open to open file "bar.txt" for writing
newFile1 = open("bar.txt", "w+")

# Use the write() method to write three lines to the file
newFile1.writelines(["This is line one\n", "This is line two\n", "this is line Threeeeeeeee\n"])
# newFile1.write("This is line one\n")
# newFile1.write("This is line two\n")
# newFile1.write("This is line three\n")

# Close the file
newFile1.close()
