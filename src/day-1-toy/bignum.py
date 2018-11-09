# Print out 2 to the 65536 power

x = 2
exponent = 65536

while exponent < 65536+1:
    n = x ** exponent
    exponent = exponent + 1
print(n)


# easier way:
print(2**65536)