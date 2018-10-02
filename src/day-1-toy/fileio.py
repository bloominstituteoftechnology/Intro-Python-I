# Use open to open file "foo.txt" for reading

f = open("src/day-1-toy/foo.txt","r")
# Print all the lines in the file
print(f.read())
# Close the file
f.close()


# Use open to open file "bar.txt" for writing
w = open("src/day-1-toy/bar.txt","w")

# Use the write() method to write three lines to the file
w.write("1\n")
w.write("2\n")
w.write("3\n")
# Close the file
w.close()