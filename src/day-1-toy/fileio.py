# Use open to open file "foo.txt" for reading
filename = "foo.txt"
file = open(filename, "r")
# Print all the lines in the file
for line in file:
	print (line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file2 = open("bar.txt", "w")
# Use the write() method to write three lines to the file
file2.writelines("\n".join(["apple", "blueberries", "cherries"]))
# Close the file
file2.close