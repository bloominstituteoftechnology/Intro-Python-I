def is_leap(year):
    leap = False

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
        print("leap1", leap)
        return leap
    print("leap2",leap)
    return leap

print("1990", is_leap(1990))
print("2000", is_leap(2000))
print("2400", is_leap(2400))
print("1800", is_leap(1800))
print("1900", is_leap(1900))
print("2100", is_leap(2100))
print("2200", is_leap(2200))
print("2300", is_leap(2300))
print("2500", is_leap(2500))
