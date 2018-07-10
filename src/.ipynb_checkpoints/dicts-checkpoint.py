# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

p1 = {
    "lat": 1,
    "long":3,
    "name": "LA1"
}

p2 = {
    "lat": 5,
    "long":7,
    "name": "LA2"
}

p3 = {
    "lat": 9,
    "long":1,
    "name": "LA3"
}
waypoints = [ p1, p2, p3
]

for wp in waypoints:
    print(wp.values())
# Write a loop that prints out all the field values for all the waypoints
