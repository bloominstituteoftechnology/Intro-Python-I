def f4(*positionals, **pairs):
	for key, value in pairs.items():
		print(f"key: {key}, value: {value}")

	for item in positionals:
		print(item)
		for key, value in item.items():
			print(f"key: {key}, value: {value}")



# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

d = {
    "monster": "goblin",
    "hp": 3
}
f4(d)