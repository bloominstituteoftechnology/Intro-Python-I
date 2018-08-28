# Use open to open file "foo.txt" for reading
foo = open("foo.txt")
# Print all the lines in the file
for l in foo:
    print(l) 
# Close the file
foo.close()


# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w')

# Use the write() method to write three lines to the filef.write
f.write('Line 1.\n')
f.write('Line 2.\n')
f.write('Line 3 Print out.\n')

# Close the file
f.close()
