d = {
    'baz': 'hi',
    'Goats': 12,
    'foo': 'bar'
}

d['Beej'] = 33

print(d['Beej'])
print(d['Goats'])

print('--------------')

for i in d:
    print(f'{i}: {d[i]}')

print('--------------')

d['Beej'] = 999999999

for k, v in d.items():
    print(f'{k}: {v}')

print('--------------')
