"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

print("""
%s
%s
%s
""" % (x, y, z))
print(f"""
{x}
{y}
{z}
""")

