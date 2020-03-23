import folium
import pandas


def color_height(elevation):
    if elevation >= 4000:
        return 'black'
    elif 3000 <= elevation < 4000:
        return 'red'
    elif 2000 <= elevation < 3000:
        return 'orange'
    elif 1000 <= elevation < 2000:
        return 'beige'
    else:
        return "green"


def radius_height(elevation):
    if elevation >= 4000:
        return 15000
    elif 3000 <= elevation < 4000:
        return 12500
    elif 2000 <= elevation < 3000:
        return 10000
    elif 1000 <= elevation < 2000:
        return 7500
    else:
        return 5000


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
    fg.add_child(folium.Circle(location=(lat, lon), popup=folium.Popup(iframe, parse_html=True),
                               radius=radius_height(elev), color=color_height(elev),
                               fill_opacity=0.7, fill=True))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:
                            {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'orange' if 20000000 <= x['properties']['POP2005'] < 30000000
                            else 'red'}))

my_map.add_child(fg)
my_map.add_child(folium.LayerControl())  # must be added AFTER (all) fg's are added

my_map.save("volcanoes_map_6.html")
