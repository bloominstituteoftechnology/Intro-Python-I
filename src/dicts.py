# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
  "lat": 42.650661,
  "lon": 18.094424,
  "name": "Dubrovnik"
  }, 
  {
  "lat": 44.786568,
  "lon": 20.448922,
  "name": "Belgrade"
  },
  {
  "lat": 50.064650,
  "lon": 19.944980,
  "name": "Krakow"
  }
]

# Write a loop that prints out all the field values for all the waypoints
for entries in waypoints:
   print('latitude: {}, longitude: {}, name: {}'.format(entries["lat"], entries["lon"], entries["name"])) 