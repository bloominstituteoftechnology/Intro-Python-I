# Use open to open file "foo.txt" for reading
open_file = open('foo.txt', 'r')
# Print all the lines in the file
print(open_file.read())
# Close the file
open_file.close()

# Use open to open file "bar.txt" for writing
new_file = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
new_file.write("here is a line \n")
new_file.write("here's another line \n")
new_file.write("and here's yet another")

# Close the file
new_file.close()
o = open('bar.txt', 'r')
print(o.read())