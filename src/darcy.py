import textwrap

print("Welcome to Darcy's Proposal, a text-based adventure game.")
print("Your goal is to propose to Miss Elizabeth Bennet and win her hand in marriage.")

print("Press 'f' for forward, 'b' for backward, 'r' for right, and 'l' for left.")

places = {
    "outside": {
        "name": "Outside Hunsford Parsonage",
        "description": "You are standing outside Hunsford Parsonage. Inside the drawing room, Elizabeth Bennet is reading a book. She is a guest of her friend Charlotte Collins, the former Miss Lucas, but the latter is away with her husband. So Miss Bennet is alone. There is a path to your right that leads to the garden, and beyond that is the forest. To your left, you will see a path that leads to Rosings Park, the residence of your aunt Lady Catherine de Bourgh. Behind you is your horse tied to a tree.", 
        "f_to": "foyer",
    },

    "foyer": {
        "name": "In the Foyer",
        "description": "The servant opens the door for you and greets you with, 'Good morning, Mr. Darcy. Yes, Miss Bennet is in. No, Mr. and Mrs. Collins are out as of the moment. They went to dine with Lady de Bourgh at Rosings. Shall I call for Miss Lizzy?'",
        "f_to": "drawing_room",
        "b_to": "outside",
    },
    ''
    "drawing_room": {
        "name": "In the Drawing Room",
        "description": "You couldn't wait for the servant to call Lizzy so you enter the drawing room to search for her. As you rehearsed your proposal rapidly inside your head, you meet Lizzy behind the door, almost bumping into her. Your presence startled her so much that she dropped the book on the floor. 'Mr. Darcy!' she exclaimed. 'Miss Bennet,' you reply. Both of you then plunged into an abyss of silence and awkwardness, your prepared speech wiped clean from your head.",
        "f_to": "elizabeth_benneth",
        "b_to": "foyer",
    },
}

class Character:
    def __init__(self, starting_place):
        self.current_place = starting_place

def direction(d, current_place):
        key = d + "_to"

        if key not in places[current_place]:
            print("You cannot go hither.")
            return current_place

        destination = places[current_place][key]

        return destination

c = Character("outside")

done = False

while not done:
    print("\n{}\n".format(places[c.current_place]["name"]))

    for line in textwrap.wrap(places[c.current_place]["description"]):
        print(line)

    s = input("\n<Command> ").strip().lower()

    if s == "q":
        done = True
    elif s in ["f", "r", "l", "b"]:
        c.current_place = direction(s, c.current_place)
    else:
        print("Unknown command {}".format(s))