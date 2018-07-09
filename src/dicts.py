# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {"lat": 10,
     "lon": 20,
     "name": "Mr. Waypoint"},
    {"lat": 100,
     "lon": 200,
     "name": "Mrs. Waypoint"},
    {"lat": 50,
     "lon": 100,
     "name": "Waypoint Jr."}
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(f'lat: {i["lat"]}, lon: {i["lon"]}, name: {i["name"]}')
