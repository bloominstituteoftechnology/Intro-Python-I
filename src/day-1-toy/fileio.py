# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r")

# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f2 = open("bar.text", "w")
# Use the write() method to write three lines to the file
f2.write("Now the file has one line!\n")
f2.write("Now the file has two lines!\n")
f2.write("Now the file has three lines!\n")

# Close the file

f2.close()
