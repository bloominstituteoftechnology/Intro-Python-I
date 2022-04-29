"""
Sets
"""
# sets are a collection of dictionary keys with no values
# with no duplicate entries

# powerful tool for calculating differences
# and intersections between other sets

# # 1. creating a set
sentence = "My name is Matt and my name is Matt and my name is Matt."
set_of_words_in_sentence = set(sentence.split())
print(set_of_words_in_sentence)

# # 2. intersection (both events)
my_party = set(["Beej", "Parth", "Sean"])
my_friends_party = set(["Parth", "Matt"])

print(my_party.intersection(my_friends_party))
print(my_friends_party.intersection(my_party))

# # 3. symmetric difference (only one event)
my_party = set(["Beej", "Parth", "Sean"])
my_friends_party = set(["Parth", "Matt"])

print(my_party.symmetric_difference(my_friends_party)) 
print(my_friends_party.symmetric_difference(my_party))

# # 4. difference (only one event and NOT the other)
my_party = set(["Beej", "Parth", "Sean"])
my_friends_party = set(["Parth", "Matt"])

print(my_party.difference(my_friends_party))
print(my_friends_party.difference(my_party))

# # 5. union (all participants)
my_party = set(["Beej", "Parth", "Sean"])
my_friends_party = set(["Parth", "Matt"])

print(my_party.union(my_friends_party))


"""
YOU DO
3 minute timer
"""
# Use the given lists to print out a set containing all
# the participants from `my_party` which did not attend
# `my_friends_party`.

my_party = ["Andy", "Bill", "Charles", "Doug", "Elliot", "Frank", "Gary", "Hank"]
my_friends_party = ["Adam", "Bill", "Charles", "Dirk", "Elliot", "Fredrick", "Gus", "Henry"]
#some setting