"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print("**********File ONE bellow**********\n\n")
file = open("foo.txt", "r")
read = file.read()
print(read, '\n\n')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print("**********File TWO bellow**********\n\n")


def song():
    bar_text = open("bar.txt", "w")
    bar_text.write("Are you ready, hey, are you ready for this?\n")
    bar_text.write("Are you hanging on the edge of your seat?\n")
    bar_text.write("Out of the doorway the bullets rip\n")
    bar_text.write("To the sound of the beat\n")
    bar_text.write("Another one bites the dust\n")
    bar_text.close()
    bar_text_read = open("bar.txt", "r")
    text = bar_text_read.read()
    print(text)


def more():
    x = "Another one bites the dust"
    more_txt = open("more_txt.txt", "w")
    for txt in range(5):
        more_txt.write(f"{x}\n")
    more_txt.close()
    more_txt_read = open("more_txt.txt", "r")
    sing_it = more_txt_read.read()
    print(sing_it)


song()
more()
