import folium

# Приклад координат (можна отримати з вашого джерела даних)
locations = [(48.8566, 2.3522), (37.7749, -122.4194), (40.7128, -74.0060)]

# Створення об'єкта мапи
my_map = folium.Map(location=[sum(x[0] for x in locations)/len(locations), sum(x[1] for x in locations)/len(locations)], zoom_start=10)

# Додавання маркерів на мапу
for loc in locations:
    folium.Marker(location=loc).add_to(my_map)

# Збереження мапи у файл (необов'язково)
my_map.save('map.html')
