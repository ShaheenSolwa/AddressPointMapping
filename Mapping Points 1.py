import folium

# Example address data
"""
LOCATION_DATA = [
("-26.2569483534662", "28.43544722183927"),
("-29.804028761006066", "30.925683452716328"),
("-29.829093334494726", "30.87076783922681"),
("-29.957622711709877", "30.968389559470193"),
("-29.908022874251735", "30.843653664358314"),
("-29.7728091466412", "30.880601695041847"),
("-29.957464689622665", "30.968362737379238"),
("-29.874359208298365", "30.913729866211156"),
("-29.722218496714284", "31.031972795911003"),
("-29.6776578675178", "31.04191376311537"),
("-29.7728091466412", "30.880601695041847"),
("-29.91519178959486", "30.906708852722566"),
("-29.77285570984258", "30.88062315271461"),
("-29.76710813490246", "30.88165030456958"),
("-29.894991354934373","30.870657366212168"),
("-29.876246820972003", "30.891056268065814"),
("-29.89273625011165", "30.878499452721222"),
("-29.996669648250034", "30.911205095054154"),
("-29.923156498380003", "30.91773263737744"),
("-29.36221154660713", "31.266673931442142"),
("-29.92998630720132", "30.903755966214163"),
("-29.638078246781905", "31.12790888154361"),
("-29.335643730232132", "31.29232258790749"),
("-26.247408837624686", "28.240301562763907"),
("-29.76587114313893", "30.88522355085958"),
("-29.92067538869054", "30.896105437377287")
]"""
LOCATION_DATA = [
("-29.908022874251735", "30.843653664358314"),
("-29.874359208298365", "30.913729866211156"),
("-29.91519178959486", "30.906708852722566"),
("-29.894991354934373","30.870657366212168"),
("-29.876246820972003", "30.891056268065814"),
("-29.89273625011165", "30.878499452721222"),
("-29.923156498380003", "30.91773263737744"),
("-29.92998630720132", "30.903755966214163"),
("-29.92067538869054", "30.896105437377287")
]


# Example address names
LOCATION_NAMES = [i for i in range(26)]

# Calculate the minimum and maximum latitudes and longitudes
min_lat = min(float(location[0]) for location in LOCATION_DATA)
max_lat = max(float(location[0]) for location in LOCATION_DATA)
min_lon = min(float(location[1]) for location in LOCATION_DATA)
max_lon = max(float(location[1]) for location in LOCATION_DATA)

# Calculate the center of the bounding box
center_location = ((max_lat + min_lat) / 2, (max_lon + min_lon) / 2)

# Calculate the radius of the circle
radius_lat = (max_lat - min_lat) / 2
radius_lon = (max_lon - min_lon) / 2
radius = 150 * (radius_lat * radius_lat + radius_lon * radius_lon) ** 0.5  # Earth's radius in km

# Create a map centered at the first location
folium_map = folium.Map(location=center_location, zoom_start=1)

# Add a marker for each location
for location, name in zip(LOCATION_DATA, LOCATION_NAMES):
    popup = folium.Popup(f"Latitude:<br>{location[0]}<br>"
                          f"Longitude:<br>{location[1]}<br>"
                          f"Name:<br>{name}",
                          background_color='white')
    folium.Marker(location=[float(location[0]), float(location[1])], popup=popup,
                  icon=folium.Icon(icon=str(name), icon_color='white')).add_to(folium_map)


# Add a circle around all the locations
folium.Circle(location=center_location,
              radius=int(radius * 1000),
              color="blue",
              fill=False,
              fill_color="blue",
              fill_opacity=0,
              popup=f"Radius: {radius} km").add_to(folium_map)

# Save the map to an HTML file
folium_map.save("Map_9_Locations.html")