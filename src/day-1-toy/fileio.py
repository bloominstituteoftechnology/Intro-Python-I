# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
for line in file:
  print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
bar = open("bar.txt", "w")


# Use the write() method to write three lines to the file
bar.write("what do you want to drink?\n")
bar.write("Gin and Juice?!\n")
bar.write("Who do you think you are, Snoop Dogg?!\n")

# Close the file
bar.close()