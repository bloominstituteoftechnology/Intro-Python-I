# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
]

waypoints.append({"lat": 234, "lon": 123, "name": "point 1" })
waypoints.append({"lat": 657, "lon": 975, "name": "point 2" })
waypoints.append({"lat": 111, "lon": 165, "name": "point 3" })

# Write a loop that prints out all the field values for all the waypoints
for entry in waypoints:
    print(entry)