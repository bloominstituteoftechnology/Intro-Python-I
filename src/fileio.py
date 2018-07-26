# Use open to open file "foo.txt" for reading
f = open("foo.txt", "rt")
# Print all the lines in the file
for x in f:
    print(x)
# Close the file
f.close()


# Use open to open file "bar.txt" for writing
bar = open('bar.txt', "rt")
# Use the write() method to write three lines to the file
lines_of_text = ["a line of text", "another line of text", "a third line"]
bar.writelines(lines_of_text)
# Close the file
bar.close()