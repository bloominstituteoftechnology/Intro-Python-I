import os
print(os.getcwd())

# Use open to open file "foo.txt" for reading
f = open(os.getcwd()+"\\src\\day-1-toy\\foo.txt")

# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open(os.getcwd()+"\\src\\day-1-toy\\bar.txt", 'w')
# Use the write() method to write three lines to the file
f.write("What is this madness?"\n)
f.write("It's fun"\n)
f.write("But silly"\n)
# Close the file
f.close()