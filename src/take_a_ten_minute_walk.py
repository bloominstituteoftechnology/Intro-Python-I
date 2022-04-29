# Take a ten minute walk from codewars
def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w"):
        return True
    else:
        return False