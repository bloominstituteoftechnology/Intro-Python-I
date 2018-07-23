# Use open to open file "foo.txt" for reading
new_file = open("foo.txt")
# Print all the lines in the file
print(new_file.read())
# Close the file
new_file.close()

# Use open to open file "bar.txt" for writing
next_file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
next_file.write("More lines to the file! \nYet another \nAnd another!")
# Close the file
next_file.close()
