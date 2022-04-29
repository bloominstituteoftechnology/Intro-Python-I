secret_n = 7
limit = 3
guess_count = 0

while guess_count < limit:
    ad = int(input("Guess: "))
    guess_count += 1
    if ad == secret_n:
        print("number founded.")
        break
else:
    print("game over.")
    
