# COUNT THE NUMBER OF LETTERS IN AN OBJECT WORKS ALSO FOR INTS
def count_letters(list_letters):
    obj = {}
    for letter in list_letters:
        if(obj.get(letter) == None):
            obj[letter] = 1
        else:
            obj[letter] += 1
    print(obj)


count_letters(['a', 'b', 'c', 'd', 'b', 'b'])
