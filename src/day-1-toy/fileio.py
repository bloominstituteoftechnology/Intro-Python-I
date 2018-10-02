# Use open to open file "foo.txt" for reading
f = open('foo.txt', "r")
# Print all the lines in the file
lines = f.readlines()
print(lines)
# Close the file
f.close()


# # Use open to open file "bar.txt" for writing
# f = open('bar.txt', 'w')

# # Use the write() method to write three lines to the file
# f.write("""line 1
# line2
# line 3""")

# # Close the file
# f.close()