import folium
import pandas


my_map = folium.Map(location=[38.58, -111.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

df = pandas.read_csv('Volcanoes.txt')

lats = list(df["LAT"])
lons = list(df["LON"])
# NAME, LOCATION, STATUS, ELEV, TYPE
names = list(df["NAME"])
locs = list(df["LOCATION"])
stats = list(df["STATUS"])
elevs = list(df["ELEV"])
types = list(df["TYPE"])

html = '''<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Location: %s<br>
Height: %s m<br><br>
Status: %s<br>
Type: %s'''

for lat, lon, name, loc, stat, elev, typ in zip(lats, lons, names, locs, stats, elevs, types):
    iframe = folium.IFrame(html=html % (name, name, loc, str(elev), stat, typ), width=350, height=175)
    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe, parse_html=True),
                               icon=folium.Icon(color='red')))

my_map.add_child(fg)
my_map.save("volcanoes_map_3.html")
