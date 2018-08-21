# Use open to open file "foo.txt" for reading

file = open("foo.txt", "r")

# Print all the lines in the file

print(file.readlines())

# Close the file

file.close()


# Use open to open file "bar.txt" for writing

file = open("bar.txt", "w")

# Use the write() method to write three lines to the file

file.write("This is the first line \n")
file.write("This is the second line \n")
file.write("This is the third line \n")


# Close the file

file.close()