import folium

# Example address data
LOCATION_DATA_1 = [
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

LOCATION_DATA_2 = [
("-29.804028761006066", "30.925683452716328"),
("-29.829093334494726", "30.87076783922681"),
("-29.957622711709877", "30.968389559470193"),
("-29.7728091466412", "30.880601695041847"),
("-29.76710813490246", "30.88165030456958"),
("-29.996669648250034", "30.911205095054154"),
("-29.76587114313893", "30.88522355085958")
]

# Calculate the minimum and maximum latitudes and longitudes for each data set
min_lat_1 = min(float(location[0]) for location in LOCATION_DATA_1)
max_lat_1 = max(float(location[0]) for location in LOCATION_DATA_1)
min_lon_1 = min(float(location[1]) for location in LOCATION_DATA_1)
max_lon_1 = max(float(location[1]) for location in LOCATION_DATA_1)

min_lat_2 = min(float(location[0]) for location in LOCATION_DATA_2)
max_lat_2 = max(float(location[0]) for location in LOCATION_DATA_2)
min_lon_2 = min(float(location[1]) for location in LOCATION_DATA_2)
max_lon_2 = max(float(location[1]) for location in LOCATION_DATA_2)

# Calculate the center of the bounding box for each data set
center_location_1 = ((max_lat_1 + min_lat_1) / 2, (max_lon_1 + min_lon_1) / 2)
center_location_2 = ((max_lat_2 + min_lat_2) / 2, (max_lon_2 + min_lon_2) / 2)

# Calculate the radius of the circle for each data set
radius_1_lat = (max_lat_1 - min_lat_1) / 2
radius_1_lon = (max_lon_1 - min_lon_1) / 2
radius_1 = 150 * (radius_1_lat * radius_1_lat + radius_1_lon * radius_1_lon) ** 0.5  # Earth's radius in km

radius_2_lat = (max_lat_2 - min_lat_2) / 2
radius_2_lon = (max_lon_2 - min_lon_2) / 2
radius_2 = 150 * (radius_2_lat * radius_2_lat + radius_2_lon * radius_2_lon) ** 0.5  # Earth's radius in km

# Create a map centered at the first location
folium_map = folium.Map(location=center_location_1, zoom_start=1)

# Add a marker for each location
for location in LOCATION_DATA_1:
    folium.Marker(location=[float(location[0]), float(location[1])],
                  icon=folium.Icon(icon=str(""), icon_color='white')).add_to(folium_map)

for location in LOCATION_DATA_2:
    folium.Marker(location=[float(location[0]), float(location[1])],
                  icon=folium.Icon(icon=str(""), icon_color='white')).add_to(folium_map)

# Add a circle around the first set of locations
folium.Circle(location=center_location_1,
              radius=int(radius_1 * 1000),
              color="blue",
              fill=False,
              fill_color="blue",
              fill_opacity=0,
              popup=f"Radius:{radius_1} km").add_to(folium_map)

# Add a circle around the second set of locations
folium.Circle(location=center_location_2,
              radius=int(radius_2 * 1000),
              color="blue",
              fill=False,
              fill_color="blue",
              fill_opacity=0,
              popup=f"Radius: {radius_2} km").add_to(folium_map)

# Save the map to an HTML file
folium_map.save("Map_16_Locations.html")