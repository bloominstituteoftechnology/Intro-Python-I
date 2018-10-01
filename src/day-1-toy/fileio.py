# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
for line in file: 
      print(line)
# Close the file

file.close()
# Use open to open file "bar.txt" for writing
file = open("bar.txt", "r")
# Use the write() method to write three lines to the file
file.write(""" working on assignment
Filling out each answer
Pushing each commit""")
# Close the file
file.close()