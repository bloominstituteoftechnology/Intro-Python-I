a = [44, 20, 129, 0]
# a = range(10)
a.insert(0, 999)
a.append(9999)

for num in a:
    print(num)

print('------------')

print(len(a))

for ii in range(len(a)):
    print(a[ii])

print('------------')


for ii in range(len(a)):
    # print(str(ii) + ': ' + str(a[ii]))
    print(f'{ii}: {a[ii]}')

print('------------')


for num in enumerate(a):
    print(num)

print('------------')

for i, v in enumerate(a):
    print(f'{i}: {v}')

print('------------')

# python list.py
# help([])
