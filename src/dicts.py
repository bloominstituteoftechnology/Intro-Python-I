# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = []
waypoints.append({'lat': 1231312, "lon": 111, "name": "Point 1"})
waypoints.append({'lat': 2222, "lon": 33333, "name": "Point 2"})
waypoints.append({'lat': 33333, "lon": 55555, "name": "Point 3"})

for x in waypoints:
    print(x['name'], x["lat"], x["lon"])
# Write a loop that prints out all the field values for all the waypoints
