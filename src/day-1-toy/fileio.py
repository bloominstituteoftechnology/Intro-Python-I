# Use open to open file "foo.txt" for reading
openFoo = open("foo.txt", "r")
# Print all the lines in the file
for words in openFoo:
    print(words)
# Close the file
openFoo.close()

# Use open to open file "bar.txt" for writing
openBar = open("bar.txt", "w")
# Use the write() method to write three lines to the file
openBar.write("Hi my name is...")
# Close the file
openBar.close()