# Use open to open file "foo.txt" for reading
fp = open("foo.txt")

# Print all the lines in the file
for line in fp:
  print(line)

# Close the file
fp.close()


# Use open to open file "bar.txt" for writing
fp = open("bar.txt", "w")

# Use the write() method to write three lines to the file
fp.write("""1st Line
2nd Line
3rd Line""")

# Close the file
fp.close()