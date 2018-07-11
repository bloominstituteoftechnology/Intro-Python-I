# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    { "lat": 51.507879, "lon": -0.087732, "name": "London Bridge"},
    { "lat": 34.134115, "lon": -118.321548, "name": "Hollywood Sign"},
    { "lat": 48.858370, "lon": 2.294481, "name": "Eiffel Tower"}
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i)
