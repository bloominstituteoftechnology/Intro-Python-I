# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

d1 = {
    "lat": 34,
    "lon": 59,
    "name": 'stash'
    }

d2 = {
    "lat": -106,
    "lon": 36,
    "name": 'money'
    }

waypoints = [d1, d2]

# Write a loop that prints out all the field values for all the waypoints\
import json

for object in waypoints:
    json_data = json.dumps(object, sort_keys=True)
    print (json_data)
