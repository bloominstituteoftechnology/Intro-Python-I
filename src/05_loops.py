"""
Python opts for a much cleaner syntax when it comes to loops compared 
to the C-style for-loops that JavaScript features. 
"""

# Use Python's `range` function with a for-loop to print the numbers 1 through 10
# YOUR CODE HERE

# Print out the numbers 1 through 10 using a while-loop
# YOUR CODE HERE 

numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
  815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
  958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
  743, 527
]

# Loop through and print out all of the even numbers from the above `numbers`
# list. Ensure that the numbers are printed in the same order in which they 
# appeart in the `numbers` list.
# Don't print out any numbers that come after 237 in the `numbers` list.
# YOUR CODE HERE
for n in numbers:
    if n == 237:
        break
    elif n % 2 == 0:
        print(n)
