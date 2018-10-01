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
#for key,value in waypoints.items():
 #   print (key, "==>",value)

for location in waypoints: 
     lat = location['lat']
     lon = location['lon']
     name = location['name']  
     print("latitude ",lat, "longitude ",lon, "name ",name) 
# Add a new waypoint to the list
