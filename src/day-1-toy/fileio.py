# Use open to open file "foo.txt" for reading
#foo = open("src/day-1-toy/foo.txt")
f = open('foo.txt', 'r')
# Print all the lines in the file
print f.read()
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open("bar.txt","w")
# Use the write() method to write three lines to the file
f.write("Hello World\n")
f.write("hello\n")
f.write("bye")
# Close the file
f.close()