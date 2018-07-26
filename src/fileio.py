# Use open to open file "foo.txt" for reading
foo = open("foo.txt", 'r')
# Print all the lines in the file
for line in foo:
  print(line)

# Close the file
foo.close

# Use open to open file "bar.txt" for writing
bar = open("bar.txt", 'w')

# Use the write() method to write three lines to the file
bar.write("On your marks...\nGet Set...\nGO!\n")

# Close the file
bar.close