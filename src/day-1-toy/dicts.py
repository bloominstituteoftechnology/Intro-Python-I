# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 715,
        "lon": 1955,
        "name": "Disneyland"
    }, 
    {
        "lat": 19,
        "lon": 65,
        "name": "Disneyworld"
    }, 
    {
        "lat": 2006,
        "lon": 9,
        "name": "Humble"
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