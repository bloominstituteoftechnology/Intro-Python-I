# Use open to open file "foo.txt" for reading
foo = open("foo.txt", "r")
# Print all the lines in the file
for line in foo:
    print(line)
# Close the file
foo.close()
# Use open to open file "bar.txt" for writing
bar = open("bar.txt", "w")
# Use the write() method to write three lines to the file
allstar = ["Somebody once told me\n", "The world is gonna roll me\n", "I ain't the sharpest tool in the shed"]
bar.writelines(allstar)
# Close the file
bar.close()
