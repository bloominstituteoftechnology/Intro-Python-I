# Use open to open file "foo.txt" for reading
file = open("foo.txt")
# Print all the lines in the file
for l in file:
  print(l)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
bar_file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
bar_file.write("He's on the scene\nUh he's the funky duck\nHe's the first to leave")

# Close the file
bar_file.close()