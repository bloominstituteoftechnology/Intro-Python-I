# Use open to open file "foo.txt" for reading
open('foo.txt', 'r')

# Print all the lines in the file
file = open('foo.txt', 'r')

print(file.read())

# Close the file

file.close()

# Use open to open file "bar.txt" for writing

file = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
file.write('Oh my goodness')
file.write('Python is totally awesome')
file.write('But also sorta hard.')

# Close the file

file.close()
