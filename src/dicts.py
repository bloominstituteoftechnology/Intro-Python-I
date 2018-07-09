# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
{"kat":453324, "piss": 1234321, "name": "Big Joy"},
{"oak":453345, "piss": 9887034, "name": "Helly Toy"},
{"hehe":45353, "piss": 1999984, "name": "Lish Moy"}
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print(i["piss"])
