# Use open to open file "foo.txt" for reading
f = open('foo.txt', 'r')
# Print all the lines in the file
if f.mode == 'r':
    contents = f.read()
    print(contents)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w+')
# Use the write() method to write three lines to the file
for i in range(3):
    f.write('This is line {}\n'.format(i+1))
# Close the file
f.close()