# Use open to open file "foo.txt" for reading
f = open('foo.text')
# Print all the lines in the file
for line in f:
    print(line)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
f.write('Hello.\nIs that you?\nReally you?\n')
# Close the file
f.close()
