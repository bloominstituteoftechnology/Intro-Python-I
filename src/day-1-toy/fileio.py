# Use open to open file "foo.txt" for reading
f = open("foo.txt")
# Print all the lines in the file
print (f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f2 = open("bar.txt", "w")
# Use the write() method to write three lines to the file
f2.write("""
hello
here's
3 lines
""")
# Close the file
f2.close()
