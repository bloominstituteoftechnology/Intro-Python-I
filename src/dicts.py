# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = {
    "lat": 90,
    "log": 15,
    "name": "home"
}

w = [ 90, 15, "home" ]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print(i)

for i in w:
    print(i)