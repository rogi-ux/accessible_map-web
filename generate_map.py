import folium
import sqlite3

def generate_map():
    try:
        conn = sqlite3.connect('accessibility.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, latitude, longitude, accessibility_features FROM locations")
        locations = cursor.fetchall()

        if not locations:
            print("No locations found. Add locations first.")
            return
        
        map = folium.Map(location=[0, 0], zoom_start=2)
        for location in locations:
            name, latitude, longitude, features = location
            popup_content = f"<b>{name}</b><br>{features}"
            folium.Marker([latitude, longitude], popup=popup_content).add_to(map)
        
        map.save("accessibility_map.html")
        print("Map generated successfully! Open accessibility_map.html to view it.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    generate_map()
