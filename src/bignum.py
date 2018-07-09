# Print out 2 to the 65536 power
i = 0
res = 0
while pow(2,i) < 65536:
  i += 1

if pow(2,i) == 65536:
    print(i)
else:
    print('Cannot find')