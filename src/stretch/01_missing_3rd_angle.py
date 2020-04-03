"""
You are given 2 out of 3 angles in a triangle, in degrees.

Write a function that classifies the missing angle 
as either "acute", "right", or "obtuse" based on its degrees.

An acute angle is less than 90 degrees.
A right angle is exactly 90 degrees.
An obtuse angle is greater than 90 degrees (but less than 180 degrees).
For example: missingAngle(11, 20) should return "obtuse", 
since the missing angle would be 149 degrees, which makes it obtuse.

More examples:
missingAngle(27, 59) ➞ "obtuse"

missingAngle(135, 11) ➞ "acute"

missingAngle(45, 45) ➞ "right"
"""
print("Give me the 1st two angles of your triangle, and I will tell you about the 3rd angle.")
first_angle = float(input("First angle (in degrees): "))
second_angle = float(input("Second angle (in degrees): "))
third_angle = 180 - first_angle - second_angle
angle_type = 'obtuse'
article = 'an'
if third_angle == 90:
    angle_type = 'right'
    article = 'a'
elif third_angle < 90:
    angle_type = 'acute'
print(
    f'Your third angle is {third_angle} degrees, which is {article} {angle_type} triangle.')
