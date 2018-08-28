# Use open to open file "foo.txt" for reading
import os
print(os.getcwd())

fp1 = open(os.getcwd()+"\\Intro-Python\\src\\day-1-toy\\foo.txt")
# Print all the lines in the file
for line in fp1:
    print(line)
# Close the file
fp.close()

# Use open to open file "bar.txt" for writing
fp2 = open(os.getcwd()+"\\Intro-Python\\src\\day-1-toy\\bar.txt", "w")
# Use the write() method to write three lines to the file
fp2.write(""" First Line
Second Line
Third Line""")
# Close the file
fp2.close()