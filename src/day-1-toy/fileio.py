# Use open to open file "foo.txt" for reading
file_name = open("foo.txt", "r")
# Print all the lines in the file
print (file_name.read())
print("-----------------------------------------------------------------")

# Close the file
file_name.close()


# Use open to open file "bar.txt" for writing
file_write = open("bar.txt", "w")


# Use the write() method to write three lines to the file
multiple_lines = ["line one\n", "line two\n", "line three\n"]
file_write.writelines(multiple_lines)

# Close the file
file_write.close()