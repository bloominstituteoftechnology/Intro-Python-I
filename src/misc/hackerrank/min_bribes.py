'''
Original queue is sorted, starting from 1, e.g. [1,2,3,4,5]
Person in queue can exchange places with person directly in front of them, up to 2 times.

If Person 5 bribes Person 4: [1,2,3,5,4]
Return the minumum number switches to get to given arrangement, or 'Too chaotic' if it would take a person more
than 2 switches to get to that arrangement.

2 1 5 3 4 -> 3 switches
2 5 1 3 4 -> Too chaotic
'''


def minimumBribes(q):
    # Try looping through nums in q.
    # If num's position < num - 3 then return 'Too chaotic'
    for i, num in enumerate(q):
        if i < num - 3:
            print('Too chaotic')
            return('Too chaotic')
    # print('Passes chaotic test')

    # Now, need to sort and keep track of how many times switches are needed to sort it.
    num_switches = 0
    made_switch = True
    while made_switch:
        current_index = 0
        made_switch = False
        while current_index < len(q) - 1:
            # print(current_index)
            if q[current_index] > q[current_index + 1]:
                # print('Time to switch')
                q[current_index], q[current_index +
                                    1] = q[current_index + 1], q[current_index]
                # print(q)
                num_switches += 1
                made_switch = True
            current_index += 1
    print(num_switches)
    return(num_switches)


print(minimumBribes([2, 1, 5, 3, 4]))  # 3 ✔️
print(minimumBribes([2, 5, 1, 3, 4]))  # Too chaotic ✔️
print(minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]))  # 1 ✔️
print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))  # Too chaotic ✔️
print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))  # 7 ✔️
