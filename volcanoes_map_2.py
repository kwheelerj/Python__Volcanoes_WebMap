import folium
import pandas


def info_str(info):
    # print(info)
    # lst = list(zip(["Name: ", "Location: ", "Status: ", "Elevation: ", "Type: "], info))
    # print(lst)
    i = 0
    s = ''
    for key, val in zip(["Name: ", "Location: ", "Status: ", "Elevation: ", "Type: "], info):
            s += key + str(val) + '\n'
            if i < 4:
                i += 1
                continue
            else:
                i = 0
                return s


my_map = folium.Map(location=[38.58, -111.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

df = pandas.read_csv('Volcanoes.txt')

lats = list(df["LAT"])
lons = list(df["LON"])
infos = df.loc[:, "NAME":"TYPE"].to_numpy()
# print(list(zip(lats, lons, infos)))

for lat, lon, info in zip(lats, lons, infos):
    fg.add_child(folium.Marker(location=[lat, lon], popup=info_str(info), icon=folium.Icon(color='red')))

my_map.add_child(fg)
my_map.save("volcanoes_map_2.html")
