def first_non_repeating_letter(string):
    char_order = []
    count = {}
    for c in string:
        if c in count: 
            count[c] += 1
        else: 
            count[c] = 1
            char_order.append(c)
    for c in char_order:
        if counts[c] == 1:
            return c
    return None