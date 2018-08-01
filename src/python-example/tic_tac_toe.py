# Python Tic-tac-toe I made.

tictactoe = [[' ', ' ', ' '], [' ', ' ', ' '],
[' ', ' ', ' ']]

for line in tictactoe:
	print(line)
print("\n")

winner = False

while winner == False:
	
	print("X's Turn\n")
	
	x = int(input("Row 1-3: "))-1
	y = int(input("Column 1-3: "))-1

	if tictactoe[x][y] == " ":
		tictactoe[x][y] = "X"

	else:
		print("\nTry again.")
		x = int(input("Row 1-3: "))-1
		y = int(input("Column 1-3: "))-1
		if tictactoe[x][y] == " ":
			tictactoe[x][y] = "X"

		else:
			print("\nTry again.")
			x = int(input("Row 1-3: "))-1
			y = int(input("Column 1-3: "))-1
			tictactoe[x][y] = "X"
	
	for line in tictactoe:
		print(line)
	print("\n")
	
	if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
		print("\nX wins the game.")
		winner = True
		continue
		
	elif " " not in tictactoe[0] and " " not in tictactoe[1] and " " not in tictactoe[2]:
		print("\nTie game.")
		winner = True
		continue
	
	print("\nO's Turn\n")
	
	x = int(input("Row 1-3: "))-1
	y = int(input("Column 1-3: "))-1

	if tictactoe[x][y] == " ":
		tictactoe[x][y] = "O"

	else:
		print("\nTry again.")
		x = int(input("Row 1-3: "))-1
		y = int(input("Column 1-3: "))-1
		if tictactoe[x][y] == " ":
			tictactoe[x][y] = "O"

		else:
			print("\nTry again.")
			x = int(input("Row 1-3: "))-1
			y = int(input("Column 1-3: "))-1
			tictactoe[x][y] = "O"
	
	for line in tictactoe:
		print(line)
	print("\n")
	
	if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][1] == "O" and tictactoe[2][1] == "O" and tictactoe[3][1] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O":
		print("\nO wins the game.")
		winner = True
		continue
		
	elif " " not in tictactoe[0] and " " not in tictactoe[1] and " " not in tictactoe[2]:
		print("\nTie game.")
		winner = True
		continue