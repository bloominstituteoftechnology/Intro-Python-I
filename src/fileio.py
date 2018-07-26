# Use open to open file "foo.txt" for reading
foo_file = open("foo.txt")

# Print all the lines in the file
print(foo_file.read())

# Close the file
foo_file.close()

# Use open to open file "bar.txt" for writing
bar_file = open("bar.txt", "w")

# Use the write() method to write three lines to the file
bar_file.write("fresh \nto \ndeath")

# Close the file
bar_file.close()