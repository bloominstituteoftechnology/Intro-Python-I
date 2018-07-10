# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.
a = {
    "lat": 35.4675602,
    "lon": -97.5164276,
    "name": "OKC"
}
b = {
    "lat": 37.7749295,
    "lon": -122.4194155,
    "name": "SFO"
}
c = {
    "lat": 51.9244201,
    "lon": 4.4777326,
    "name": "ROT"
}

waypoints = [a, b, c]

print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(f'The name of the waypoint is {i["name"]}. It sits at latitude {i["lat"]}, longitude {i["lon"]}.')