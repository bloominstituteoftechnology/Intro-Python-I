def feed():
    eating = [True, False, True, False, False]
    i = 0
    c = 0
    while c < 10:
        if i == 0:
            if eating[4]:
                eating[4] = False
                eating[i] = True
        else:
            if eating[i-1]:
                eating[i-1] = False
                eating[i] = True
        i = (i + 1) % 5
        c = c + 1
        print(eating)

feed()
