# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 34.046145,
        "lon": -118.345499,
        "name": "Leo's Tacos"
    },
    {
        "lat": 34.096467,
        "lon": -118.389694,
        "name": "Dr Dre's House"
    },
    {
        "lat": 37.800286,
        "lon": -122.437998,
        "name": "Izzy's"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for place in waypoints:
    print(place['name'], place['lat'], place['lon'])