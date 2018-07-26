# Use open to open file "foo.txt" for reading
foo = open("foo.txt", "r")

# Print all the lines in the file
for x in foo.readlines():
  print(x)

# Close the file
foo.close()

# Use open to open file "bar.txt" for writing
bar = open("bar.txt", "w")

# Use the write() method to write three lines to the file
for x in range(3):
  bar.write("This is line %d\r\n" % (x + 1))

# Close the file
bar.close()