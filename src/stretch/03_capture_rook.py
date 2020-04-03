"""Return true if two rooks can attack each other, and false otherwise.

Examples:
canCapture(["A8", "E8"]) ➞ true

canCapture(["A1", "B2"]) ➞ false

canCapture(["H4", "H3"]) ➞ true

canCapture(["F5", "C8"]) ➞ false

Notes:

Assume no blocking pieces.
Two rooks can attack each other if they share the same row (letter) or column (number).
"""

print("Give me the position of two rooks, and I'll tell you if they can attack each other.")
rook1_row = input("Rook 1 Row (A-H): ")
rook1_col = input("Rook 1 Column (1-8): ")
rook2_row = input("Rook 2 Row (A-H): ")
rook2_col = input("Rook 1 Row (1-8): ")

rook1 = rook1_row + rook1_col
rook2 = rook2_row + rook2_col

can_attack = False
word = "can't"
if (rook1[0] == rook2[0]) or (rook1[1] == rook2[1]):
    can_attack = True
    word = "can"

print(f'{rook1} and {rook2} {word} attack each other!')
if can_attack:
    print("Charge!!")
else:
    print("Too bad.")
