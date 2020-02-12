# RPS game
import random

moves = ["r","p","s"]
wins = 0
losses = 0
ties = 0

while True:
    cmd = input("~~~~~~")

    cpu_move = random.choice(moves)
    print(f"Cpu picks {cpu_move}")
    if cmd == "r":
        if cpu_move == "r":
            print("You tie!")
            ties += 1
            
        elif cpu_move == "p":
            print("You lost!")
            losses += 1
            
        elif cpu_move == "s":
            print("You Win!")
            wins += 1
            
    elif cmd == "p":
        if cpu_move == "r":
            print("You Win!")
            wins += 1
            
        elif cpu_move == "p":
            print("You tie!")
            ties += 1
            
        elif cpu_move == "s":
            print("You lost!")
            losses +=1
            
    elif cmd == "s":
        if cpu_move == "r":
            print("You lost!")
            losses += 1
            
        elif cpu_move == "p":
            print("You Win!")
            wins += 1
           
        elif cpu_move == "s":
            print("You tie!")
            ties += 1
    elif cmd ==  "q":
        print("bye")
        break
    else:
        print("Input r,p,s, or q")
    print(f"Wins: {wins}, Losses: {losses}, Ties {ties}")
