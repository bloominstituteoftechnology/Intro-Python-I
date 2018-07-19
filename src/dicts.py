# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {"lat": "48.8584° N", "lon": "2.2945° E", "name": "Eiffel Tower"},
    {"lat": "40.6892° N", "lon": "74.0445° W", "name": "Statue of Liberty"},
    {"lat": "22.9519° S", "lon": "43.2105° W", "name": "Christ The Redeemer"},
]

# Write a loop that prints out all the field values for all the waypoints
# places = [i["name"] for i in waypoints]
# print(places)
nl = "\n"
for place in waypoints:
    for k, v in place.items():
        print(f"{k}: {v}")
