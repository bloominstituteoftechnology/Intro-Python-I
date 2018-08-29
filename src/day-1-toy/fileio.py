foo = open("src/day-1-toy/foo.txt", "r")
print(foo.read())
# Close the file
foo.close()

# Use open to open file "bar.txt" for writing
bar = open("src/day-1-toy/bar.txt", "w")
lines = ["line1\n", "line2\n", "line3\n"]
bar.writelines(lines)
bar.close()


# Use the write() method to write three lines to the file

# Close the file
