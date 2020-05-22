def countingValleys(n, s):
    # n is number of steps
    # s is string of his path ie [DDUUUUDD]
    # Assume he starts at sea level
    if n == 0:
        print("No steps")
        return 0
    num_valleys = 0  # -1
    current_level = 0
    for step in s:
        print(step)
        if step == 'D':
            current_level -= 1
            print("current_level " + str(current_level))
        elif step == 'U':
            current_level += 1
            print("current_level " + str(current_level))
            if current_level == 0:
                num_valleys += 1
    print("current_level at end " + str(current_level))
    print(num_valleys)
    return num_valleys


# countingValleys(8, 'DDUUUUDD') # 1
# countingValleys(8, 'UDDDUDUU')  # 1 test case 0
# countingValleys(8, 'DDUUDDUDUUUD')  # 2
# countingValleys(12, 'DDUUDDUDUUUD')  # 2 test case 1
# countingValleys(0, '')
