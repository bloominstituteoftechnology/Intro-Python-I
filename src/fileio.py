# Extract path from current file location
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# Use open to open file "foo.txt" for reading
# append current file location to filepath argument when opening for reading
f = open(dir_path + '\\' + 'foo.txt', 'r')

# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
b = open(dir_path + '\\' + 'bar.txt', 'w')
# Use the write() method to write three lines to the file
b.write('This is a line sir, and I do not bite!\nThis is yet another line, I BITE YA NOW!')
# Close the file
b.close()