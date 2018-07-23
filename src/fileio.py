# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r", encoding="utf-8")

# Print all the lines in the file
for line in f: 
    print(line)

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open("bar.txt", "w+", encoding="utf-8")

# Use the write() method to write three lines to the file
f.writelines(["One Line\n", "Two Lines\n", "Three Lines\n"])

# Close the file
f.close()