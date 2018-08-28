# Use open to open file "foo.txt" for reading
open("foo.txt", "r")
# Print all the lines in the file
print(open("foo.txt", "r").read())
# Close the file
open("foo.txt", "r").close()

# Use open to open file "bar.txt" for writing
open("bar.txt", "a")
# Use the write() method to write three lines to the file
open("bar.txt", "a").write("\n Hello \n World \n !")
# Close the file
open("bar.txt", "a").close()
