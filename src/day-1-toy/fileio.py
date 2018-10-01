# Use open to open file "foo.txt" for reading
foo = open("foo.txt")

# Print all the lines in the file
for i in foo:
    print(i)

# Close the file
foo.close()

# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/
# Use open to open file "bar.txt" for writing
bar = open("bar.txt", "w")

# Use the write() method to write three lines to the file
bar.write( )

# Close the file