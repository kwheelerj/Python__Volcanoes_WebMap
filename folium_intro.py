import folium

my_map = folium.Map(location=[38.58, -99.09], zoom_start=7, tiles="Stamen Terrain")
print(type(my_map))

# my_map.add_child(folium.Marker(location=[38.2, -99.1], popup='Hi, I am a marker', icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup='Hi, I am a marker', icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[37.2, -97.1], popup='Hi, I am a marker 2', icon=folium.Icon(color='blue')))

for coordinates in [ [36.2, -97.1], [35.6, -97.6] ]:
    fg.add_child(folium.Marker(location=coordinates, popup='marker', icon=folium.Icon(color='red')))

my_map.add_child(fg)

my_map.save("Map1.html")
