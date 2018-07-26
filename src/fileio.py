# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
for line in file:
  print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w+")

# Use the write() method to write three lines to the file
file.write(""" Once there was a girl
who attended a school named Lambda
to learn to code
""")

# Close the file
file.close()
