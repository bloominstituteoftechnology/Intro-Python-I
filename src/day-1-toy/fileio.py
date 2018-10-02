import os

# Use open to open file "foo.txt" for reading
path = 'src/day-1-toy/foo.txt'
file = open(path, 'r')

# Print all the lines in the file

print(file.read())

# Close the file

file.close()

# Use open to open file "bar.txt" for writing

file = open(path, 'a')

# Use the write() method to write three lines to the file

file.write("\nOr a squirrel, sir?")
file.write("\nIf only a quarrelsome squirrel, sir.")
file.write("\nDeal.")


# Close the file

file.close()