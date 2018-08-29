# Write a class to hold player information, e.g. what room they are in
# currently.

#Put the Player class in `player.py`.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    # def __iter__(self):
    #     self.key_index = 0
    #     return self

    # def __next__(self):
    #     test = self.key_index
    #     if test > 5:
    #         raise StopIteration
    #     self.key_index = test + 1
    #     return test

# p1 = Player('Adrian', 'Living Room')

# # print(p1.__dict__)
# # print(p1.name)
# # print(p1.location)

# for key in p1.__dict__:
#     if key == 'location':
#         print(p1.location)


# for key in p1:
#     print(p1.location)

