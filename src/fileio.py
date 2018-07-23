# Use open to open file "foo.txt" for reading

# Print all the lines in the file
f = open("foo.txt", "r")
for each in f:
    print(each)
f.close()

# Close the file


# Use open to open file "bar.txt" for writing
fo = open("foo.txt", "w")
fo.write("""HellOWorld
poop
DOOOOOOOOOOOOOOOOOOOO""") 
fo.close()

# Use the write() method to write three lines to the file

# Close the file