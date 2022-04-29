def find_even_index(arr):
    zrr=[]
    for i in range(len(arr)):
        if i==0:
            if sum(zrr)==sum(arr)-arr[0]:
                return i
        elif i>=1:
            zrr.append(arr[i-1])
            if sum(zrr)==sum(arr)-arr[i]-sum(zrr):
                return i
    else:
        return -1