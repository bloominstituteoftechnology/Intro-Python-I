# Use open to open file "foo.txt" for reading
file = open("C:\\Users\\Borg\\Desktop\\webdev\\lambdaSchool\\gitProjects\\Intro-Python\\src\\day-1-toy\\foo.txt","r")
# Print all the lines in the file
for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("C:\\Users\\Borg\\Desktop\\webdev\\lambdaSchool\\gitProjects\\Intro-Python\\src\\day-1-toy\\bar.txt","w")
# Use the write() method to write three lines to the file
lines_of_text = ["a line of text", "another line of text", "a third line"]
file.writelines(lines_of_text)
file.close()
# Close the file
