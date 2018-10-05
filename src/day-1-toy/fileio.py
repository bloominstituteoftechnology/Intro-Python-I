# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r")
# Print all the lines in the file
lines = f.read() 
print(lines)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
with open("bar.txt", "w") as file:
    file.write("Line 1 is here.")
    file.write("line 2 is here.")
    file.write("Line 3 is here.")
# Close the file
file.close()