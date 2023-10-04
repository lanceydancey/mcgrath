import exifread
import glob
import folium
import pandas as pd
from folium.plugins import FastMarkerCluster
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

filenames = glob.glob("*.jpeg")

TAGS = 'GPS GPSLatitudeRef,GPS GPSLatitude,GPS GPSLongitudeRef,GPS GPSLongitude'.split(',')

def gps_dms2dd(lat, lon, lat_dir, lon_dir):
    dd_lat = float(lat[0]) + float(lat[1])/60 + float(lat[2]) / 3600
    #print(lat_dir)
    if lat_dir == 'S': 
        dd_lat *= -1
    dd_lon = float(lon[0]) + float(lon[1])/60 + float(lon[2]) / 3600
    if lon_dir == 'W': 
        dd_lon *= -1
    
    return dd_lat, dd_lon

ls = []
for filename in filenames:
    f = open(filename, 'rb')
    tags = exifread.process_file(f)
    f.close()
    if tags:
        if TAGS[1] in tags:
            lat, lon = gps_dms2dd(tags[TAGS[1]].values, tags[TAGS[3]].values, tags[TAGS[0]].values, tags[TAGS[2]].values)
            ls.append([lat, lon, filename])
            print(filename, lat, lon)
df = pd.DataFrame(ls, columns=['latitude', 'longitude','filename'])

lat, lon, f = df[["latitude", "longitude","filename"]].values.tolist()[0]

folium_map = folium.Map(
    location=[lat, lon], zoom_start=12, tiles="cartodbpositron"
)

callback = (
    "function (row) {"
    'var marker = L.marker(new L.LatLng(row[0], row[1]), {color: "red"});'
    "var icon = L.AwesomeMarkers.icon({"
    "icon: 'info-sign',"
    "iconColor: 'white',"
    "markerColor: 'green',"
    "prefix: 'glyphicon',"
    "extraClasses: 'fa-rotate-0'"
    "});"
    "marker.setIcon(icon);"
    "var popup = L.popup({maxWidth: '300'});"
    "const display_text = {text: row[2]};"
    "var mytext = $(`<div id='mytext' class='display_text' style='width: 100.0%; height: 100.0%;'> ${display_text.text}</div>`)[0];"
    "popup.setContent(mytext);"
    "marker.bindPopup(popup);"
    "return marker};"
)

FastMarkerCluster(
    df[["latitude", "longitude","filename"]].values.tolist(), callback=callback
).add_to(folium_map)

# data=list(zip(df['latitude'].values, df['longitude'].values))
# marker_cluster = MarkerCluster().add_to(folium_map)

# for point in range(0, len(data)):
#     try:
#         folium.Marker(data[point], popup = folium.Popup(df[point]['Name'])).add_to(marker_cluster)
#     except:
#         pass
# df.apply(lambda row:folium.CircleMarker(location=[row["latitude"], row["longitude"]], tooltip=row["Name"]).add_to(folium_map), axis=1)
# folium.TileLayer('cartodbdark_matter', attr="cartodb").add_to(folium_map)
# folium.TileLayer('openstreetmap',attr="openstreepmap").add_to(folium_map)
# folium.LayerControl().add_to(folium_map)
#folium_map

folium_map.save("map3.html")
        
        
