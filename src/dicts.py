# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [{"lat": 7, "lon": 2, "name": "First"},
             {"lat": 12, "lon": 52, "name": "Second"},
             {"lat": 42, "lon": 25, "name": "Third"}]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i['lat'], i['lon'], i['name'])
