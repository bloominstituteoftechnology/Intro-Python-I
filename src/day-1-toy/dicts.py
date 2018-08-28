# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 47.606209,
        "lon": -122.332069,
        "name": "Seattle, WA"
    },
    {
        "lat": 21.967580,
        "lon": -159.357960,
        "name": "Kauai, Hawaii"
    },
    {
        "lat": 10.605903,
        "lon": 119.499662,
        "name": "Palawan, Philippines"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for city in waypoints:
    print('{}: latitude = {}, longitude = {}'.format(city["name"], city["lat"], city["lon"]))
# Add a new waypoint to the list
waypoints.append({
    "lat": 23.45,
    "lon": -123,
    "name": "Bombadil's House"
})
print(waypoints)
