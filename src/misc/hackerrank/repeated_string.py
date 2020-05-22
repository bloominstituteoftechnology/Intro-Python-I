def repeatedString(s, n):
    # s is the 'word' - what needs to be repeated to be at least n long
    # n is how long of a string we are considering
    # Return the number of occurrences of 'a' in string[0:n]
    if s == 'a':
        print(n)
        return n
    elif s.index('a') == -1:
        print("No a's")
        return 0
    my_string = s
    while len(my_string) < n:
        my_string += my_string
    # print(my_string)
    num_as = 0
    for i in range(0, n):
        if my_string[i] == 'a':
            num_as += 1
    print(num_as)
    return num_as


# repeatedString('abcac', 10) # 4
# repeatedString('aba', 10)  # 7
# repeatedString('a', 1000000000000)


def repeatedString2(s, n):
    if s == 'a':
        print(n)
        return n
    elif s.index('a') == -1:
        print("No a's")
        return 0

    elif n < len(s):
        print("Deal")

    # Find num of a's in a single s
    # num = len([i for i, x in enumerate(s) if x == "a"])
    num = s.count('a')
    print("number of a's in s: " + str(num))

    # Calculate if there will be extra letters needed after n // len(s) to get the repeated string to be n long
    leftover = n % len(s)
    print("leftover: " + str(leftover))
    # Calculate total num of a's if n % len(s) == 0
    total = num * (n // len(s))
    print(total)
    # Now, add the number of a's in that leftover part of the repeated string
    '''
    for i in range(leftover):
        if s[i] == 'a':
            total += 1
    '''
    total += s[:leftover].count('a')
    print("Final total: " + str(total))
    return total


repeatedString2('aba', 10)
# repeatedString2('abcac', 10)
# repeatedString2('a', 1000000000000)
# repeatedString2('abababab', 3)
# repeatedString2('ababababdfjklsd;asldkf', 3)


def repeatedString3(s, n):
    answer = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    print(answer)
    return answer


# repeatedString3('abababab', 3)
