import folium
from folium.plugins import PolyLineTextPath

# Create a base map centered on South Korea
south_korea_map = folium.Map(location=[36.5, 127.5], zoom_start=8, tiles='OpenStreetMap')

# Define colors for each day (marker icons)
day_colors = {
    1: 'blue',
    2: 'green',
    3: 'purple',
    4: 'orange',
    5: 'darkred',
    6: 'cadetblue'
}

# Full itinerary in travel order (day, "Site Name", latitude, longitude)
all_stops = [
    # Day 1
    (1, "Paju DMZ", 37.9160, 126.7831),
    (1, "Lotte Tower Seoul Sky", 37.5125, 127.1028),
    
    # Day 2
    (2, "Seoraksan Mountain", 38.1194, 128.4656),
    (2, "Naksansa Temple", 38.1235, 128.6285),
    
    # Day 3
    (3, "Hahoe Folk Village", 36.5407, 128.5183),
    (3, "Dosan Seowon", 36.5378, 128.7376),
    
    # Day 4
    (4, "Bulguksa Temple", 35.7904, 129.3326),
    (4, "Seokguram Grotto", 35.7941, 129.3494),
    (4, "Donggung and Wolji Pond", 35.8345, 129.2247),
    (4, "Haeundae Beach", 35.1580, 129.1603),
    
    # Day 5
    (5, "Gamcheon Cultural Village", 35.0975, 129.0103),
    (5, "Jagalchi Fish Market", 35.0969, 129.0364),
    
    # Day 6
    (6, "Gyeongbokgung Palace", 37.5796, 126.9770),
    (6, "Bukchon Hanok Village", 37.5826, 126.9836)
]

# Prepare a list of (lat, lon) for the continuous route
line_coords = []

# Add markers for each stop (color-coded by day)
for day, site_name, lat, lon in all_stops:
    marker_color = day_colors.get(day, 'blue')
    folium.Marker(
        location=[lat, lon],
        popup=f"Day {day}: {site_name}",
        tooltip=f"Day {day}: {site_name}",
        icon=folium.Icon(color=marker_color, icon='info-sign')
    ).add_to(south_korea_map)
    line_coords.append((lat, lon))

# Draw a continuous polyline for the entire itinerary
route_line = folium.PolyLine(
    locations=line_coords,
    color='red',
    weight=3,
    opacity=0.8
).add_to(south_korea_map)

# Add arrowheads along the route to indicate direction
PolyLineTextPath(
    route_line,
    '   ►   ',
    repeat=True,
    offset=7,
    attributes={'fill': 'red', 'font-weight': 'bold', 'font-size': '14'}
).add_to(south_korea_map)

# Add explicit START and END markers with distinct icons
start_lat, start_lon = line_coords[0]
end_lat, end_lon = line_coords[-1]

folium.Marker(
    location=[start_lat, start_lon],
    popup="START",
    tooltip="START",
    icon=folium.Icon(color='darkgreen', icon='play')
).add_to(south_korea_map)

folium.Marker(
    location=[end_lat, end_lon],
    popup="END",
    tooltip="END",
    icon=folium.Icon(color='darkred', icon='stop')
).add_to(south_korea_map)

# Save the map to an HTML file
map_filename = "south_korea_itinerary_with_start_end.html"
south_korea_map.save(map_filename)
print(f"Map generated: {map_filename}")
