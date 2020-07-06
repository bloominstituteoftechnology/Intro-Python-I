def tickets(people):
    change = 0
    print(people)
    for num, bill in enumerate(people):
        print("this is the current bill", bill, "with the index of", num, "here is the change", change)
        if bill > 25:
            if bill - 25 > change:
                return "NO"
            change = change - (bill - 25)
            print("this is change after the payment", change)
        else:
            change = change + 25
            print("this is change after the payment", change)
    return "YES"

def tickets(people):
    d25 = 0
    d50 = 0
    d100 = 0
    for i in people:
        if i == 25:
            d25+=1
        elif i == 50:
            if d25 >= 1:
                d50+=1
                d25-=1
            else:
                return 'NO'
        else:
            if (d50 >=1 and d25 >=1):
                d100+=1
                d50-=1
                d25-=1
            elif d25 >=3:
                d100+=1
                d25-=3
            else:
                return 'NO'
    return 'YES'