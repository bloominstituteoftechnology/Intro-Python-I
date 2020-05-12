"""
python3 store.py
The Dugout
  1. Running
  2. Baseball
  3. Basketball
  4. Exit
Select the number of a department

Attributes:
- name
- departments

Optional extra attributes:
- Store hours
- Store capacity
"""

# Composition: a "has-a"

from departments import Department

class Store:
	def __init__(self, name, departments):
		self.name = name
		self.departments = []

		for dep in departments:
			department = Department(dep)
			self.departments.append(department)

	def __str__(self):
		output = ""
		output += self.name+"\n"
		for index, department in enumerate(self.departments):
			output += str(index+1)+". "+str(department)+"\n"
		output += str(len(self.departments)+1)+". Exit"
		return output

store = Store("The Dugout", ["Running", "Baseball", "Basketball", "Fencing"])
print(store)

selection = 0
while selection != len(store.departments)+1:
	selection = input("Select the number of a department. ")
	try:
		selection = int(selection)
		if selection >= 1 and selection < len(store.departments)+1:
			print(f"The user selected: {selection}")
		else:
			print("Please choose from the provided choices.")
	except ValueError:
		print("Choose a number, not an empty string or a letter or something.")

print("Thank you for shopping with us today! :-)")
