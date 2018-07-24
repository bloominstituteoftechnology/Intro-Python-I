# Use open to open file "foo.txt" for reading
txt = open('foo.txt')
# Print all the lines in the file

# Close the file
print(txt.read())
txt.close()
# Use open to open file "bar.txt" for writing
txt2 = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
lines = {
'line1' : input("What would you like to write? "),
'line2' : input("Another line please "),
'line3' : input("Last one I swear ")
}


for i in lines:
    lines[i]
    txt2.write(lines[i])

# Close the file
txt2.close()
