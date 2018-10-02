# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

dictionary = [
    {
        "Lat": "40.7128 N",
        "Lon": "74.0060 W",
        "name": "New York City",
    },
    {
        "Lat": "33.7175 N",
        "Lon": "117.8311 W",
        "name": "Orange County",
    },
    {
        "Lat": "28.3852 N",
        "Lon": "81.5639 W",
        "name": "Disney World",
    }
]

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
# for i in waypoints:
#     print(i)

# Add a new waypoint to the list
waypoints.append(    {
        "at": 28.3852,
        "Lon": 81.5639,
        "name": "Disney World",
    })

for i in waypoints:
    print(i)