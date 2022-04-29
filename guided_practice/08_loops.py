"""
Loops
"""

# # 1. "for" loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# # Prints out the numbers 0,1,2,3,4
for x in range(5):
     print(x)

# # Prints out 3,4,5
for x in range(3, 6):
     print(x)

# # Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# # 2. "while" loop
# # Prints out 0,1,2,3,4

count = 0
while count < 5:
     print(count)
     count += 1  # This is the same as count = count + 1

# # 3. "break" and "continue"
#  Prints out 0,1,2,3,4

count = 0
while True:
     print(count)
     count += 1
     if count >= 5:
         break

# # Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
#     # Check if x is even
     if x % 2 == 0:
         continue
     print(x)

"""
YOU DO
3 minute timer
"""
# Take the numbers list that is provided and do the following:
# print all the odd numbers (but don't print any numbers after 412)
numbers = [
     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
     743, 527
 ]
#print(odds & 412)