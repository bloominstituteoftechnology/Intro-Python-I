# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, playerName, startLocation):
        self.name = playerName
        self.location = startLocation

    
# p1 = Player('Adrian', 'Living Room')
# print(p1.__dict__)
# print(p1.name)
# print(p1.location)



##ASIDE
# for key in p1.__dict__:
#     if key == 'location':
#         print(p1.location)




