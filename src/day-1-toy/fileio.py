# Use open to open file "foo.txt" for reading

foo = open("src/day-1-toy/foo.txt")

# Print all the lines in the file

for line in foo:
    print(line)

# Close the file

foo.close()

# Use open to open file "bar.txt" for writing

foo = open("src/day-1-toy/foo.txt", 'w')

# Use the write() method to write three lines to the file

foo.write("afkasdjhfalksdjf")
foo.write("qdsfasdgvasdgaggs")
foo.write("dafsdgasagsdf")

# Close the file

foo.close()
