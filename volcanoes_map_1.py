import folium
import pandas


my_map = folium.Map(location=[38.58, -111.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

df = pandas.read_csv('Volcanoes.txt')

coordinates_data = (df.loc[:, 'LAT':'LON']).to_numpy()
# print(coordinates_data)
for coordinates in coordinates_data:
    fg.add_child(folium.Marker(location=coordinates, popup='marker', icon=folium.Icon(color='red')))


my_map.add_child(fg)
my_map.save("volcanoes_map_1.html")
