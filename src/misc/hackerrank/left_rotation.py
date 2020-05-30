'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true&h_r=next-challenge&h_v=zen


A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array [1,2,3,4,5] , then the array would become [3,4,5,1,2].

Given array a of n integers (n is not used in the rotLeft() function)
and a num d,
perform d left rotations on the array.

Format to return: A single line of space-separated ints.

'''

# For each left rotation, arr[0] is popped from the arr and added to the end of the arr.


def rotLeft(a, d):
    '''
    # If you don't want to modify original arr
    new_a = a[:]
    for i in range(d):
        first_el = new_a[0]
        new_a = new_a[1:]
        new_a.append(first_el)
        print(new_a)
    '''
    '''
    # If it's okay to modify original arr
    for i in range(d):
        first_el = a[0]
        a = a[1:]
        a.append(first_el)
        # print(a)
    '''

    # A more time efficient way would be to NOT loop, but just do 1 cut and paste.
    # Find initial chunk to cut, from beginning to just before d.
    # Get rest of arr
    # Append initial chunk to the rest of arr
    '''
    first_els = a[:d]
    a = a[d:]
    a = a + first_els
    '''
    # More concise way
    a = a[d:] + a[:d]
    '''
    for num in a:
        print(str(num), end=" ")
    '''
    return a


print(rotLeft([1, 2, 3, 4, 5], 4))
