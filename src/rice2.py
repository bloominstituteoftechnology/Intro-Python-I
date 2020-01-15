def feed():
    eating = [True, False, True, False, False]
    c = 0
    while c < 10:
        print(eating)
        first = eating.index(True)
        second = eating.index(True, first + 1)
        eating[first] = False
        eating[(first + 1) % 5] = True
        eating[second] = False
        eating[(second + 1) % 5] = True
        c = c + 1

feed()
