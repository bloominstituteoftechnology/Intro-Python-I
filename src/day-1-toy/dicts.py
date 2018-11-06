# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "Spain"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "Colombia"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "Mexico"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for item in waypoints:
    print(item.values())

"""
Alternative:

for w in waypoints:
  print(w['name'], w['lat'], w['lon'])
"""

# Add a new waypoint to the list
waypoints.append({
    "lat": 22,
    "lon": -181,
    "name": "Texas"
})

print(waypoints)
