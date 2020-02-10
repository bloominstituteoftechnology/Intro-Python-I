"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("./foo.txt", "rb") as reading:
    for x in reading.readlines():
        print(x)
    reading.close()
    
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "w") as writing:
    lines = ["Alas, my heart's queen! alas, my wife! \nMy heart's lady, ender of my life!",
            "What is this world? What do men ask to have? \nNow with his love, now in his cold grave",
            "Alone, without any company. \nFarewell, my sweet foe, my Emily!"]
    for i in lines:
        writing.write(f"{i}\n")
    writing.close()
