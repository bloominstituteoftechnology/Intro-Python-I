# Use open to open file "foo.txt" for reading
with open('foo.txt') as textFile:
  text = textFile.read()
print(text)

# Print all the lines in the file

# Close the file


# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file
lines = ["line1", "line2", "line3"]

with open("bar.txt", "w") as f:
  for line in lines:
    f.write(line)
    f.write("\n")
    #print(line)