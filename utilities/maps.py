import gmplot
import webbrowser
import geocoder
from geopy.geocoders import Nominatim
import json, urllib
from urllib.parse import urlencode
import googlemaps

#destination
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Powai Mumbai")

#source
g = geocoder.ip('me')

api_key="key=AIzaSyA7Dfm5_owPuczra0Ey8TsE92PDf1-RC8s"
str_origin = "origin=" + str(g.latlng[0]) + "," + str(g.latlng[1]);
str_dest = "destination=" + str(getLoc.latitude) + "," + str(getLoc.longitude);
sensor = "sensor=true";
mode = "mode=driving";
parameters = str_origin + "&" + str_dest + "&" + sensor + "&" + mode + "&" + api_key;
output = "json";
url = "https://maps.googleapis.com/maps/api/directions/" + output + "?" + parameters;
print(url)
# url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
#             ('origin', start),
#             ('destination', finish)
#  ))
# print(url+"&key =" +api_key )
ur = urllib.request.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
    print (j)

# calling the Nominatim tool
# loc = Nominatim(user_agent="GetLoc")
 
# # entering the location name
# getLoc = loc.geocode("Powai Mumbai")
 
# # printing address
# # print(getLoc.address)
 
# # printing latitude and longitude
# # print("Latitude = ", getLoc.latitude, "\n")
# # print("Longitude = ", getLoc.longitude)

# g = geocoder.ip('me')
# # print(g.latlng)

  
# latitude_list = [ g.latlng[0], getLoc.latitude ]
# longitude_list = [ g.latlng[1], getLoc.longitude ]
  
# gmap3 = gmplot.GoogleMapPlotter(g.latlng[0],
#                                 g.latlng[1], 12)
  
# # scatter method of map object 
# # scatter points on the google map
# gmap3.scatter(latitude_list, longitude_list, '#FF0000',size = 40, marker = False)
  
# # Plot method Draw a line in
# # between given coordinates
# gmap3.plot(latitude_list, longitude_list,'cornflowerblue', edge_width = 2.5)
  
# gmap3.draw(r"C:\Users\patil\Desktop\map13.html")
# webbrowser.open_new_tab(r"C:\Users\patil\Desktop\map13.html")