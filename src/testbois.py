import random
playing = True


class Knight:
    def __init__(self, name, hp, att, dfns):
        self.name = name
        self.hp = hp
        self.att = att
        self.dfns = dfns


Player1 = Knight('Willifred', 100, 5, 5)
Player2 = Knight('Fontaine', 100, 5, 5)
while playing == True:

    print(Player1.name, " just challenged ", Player2.name)

    def attack(attack, victimDef, victimObj):

        if(attack > victimDef*random.random()+(victimDef/2)):
            damageref = victimObj.hp
            victimObj.hp -= 25*random.random()
            print(victimObj.name, " was hit for ",
                  damageref - victimObj.hp, " damage!")

        else:
            print("attack missed!")

    response = input("Do you accept this challenge (type yes) -:  ")
    if(response == "q"):
        print("thanks for playing")
        playing = False
    elif(response == "yes"):
        print(Player2.hp)
        attack(Player1.att, Player2.dfns, Player2)
        print(Player2.hp)
        if(Player2.hp <= 0):
            print("Game over, ", Player2.name, " is dead.")
            playing = False

    else:
        print("sure, okay. type q if you want to quit or something")
