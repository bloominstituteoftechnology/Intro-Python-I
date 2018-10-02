
import random

def get_random_rps():
    rps = ["r", "p", "s"]
    return rps [random.randrange(0, 3)]

while True: 
    agent_choice = get_random_rps()
    cmd = input("=>")
    if cmd == "q":
        break
    elif cmd == "r" or cmd == "p" or cmd == "s" 
        print(cmd)