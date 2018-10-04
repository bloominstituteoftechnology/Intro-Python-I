import os

# Use open to open file "foo.txt" for reading
cwd = os.getcwd()
files = os.listdir(cwd)
print(files)
o = open("src/day-1-toy/foo.txt", "r")
# Print all the lines in the file
print(o.read())
# Close the file
o.close()

# Use open to open file "bar.txt" for writing
o = open("bar.txt", "w")
# Use the write() method to write three lines to the file
add = [1,2,3]
for num in add:
    o.write(str(num))
    o.write("\n")
# Close the file
o.close()