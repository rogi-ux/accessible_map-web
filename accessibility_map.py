import sqlite3
import folium

# Connect to the database
conn = sqlite3.connect('accessibility.db')
cursor = conn.cursor()

def add_location():
    name = input("Enter location name: ")
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    accessibility = input("Enter accessibility feature (e.g., wheelchair ramp): ")
    
    cursor.execute(
        "INSERT INTO locations (name, latitude, longitude, accessibility) VALUES (?, ?, ?, ?)",
        (name, latitude, longitude, accessibility),
    )
    conn.commit()
    print("Location added successfully!")

def view_locations():
    cursor.execute("SELECT * FROM locations")
    rows = cursor.fetchall()
    if rows:
        print("\nStored Locations:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Latitude: {row[2]}, Longitude: {row[3]}, Accessibility: {row[4]}")
    else:
        print("\nNo locations found.")

def delete_location():
    location_id = input("Enter the ID of the location to delete: ")
    try:
        cursor.execute("DELETE FROM locations WHERE id = ?", (location_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Location deleted successfully!")
        else:
            print("No location found with the provided ID.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_locations():
    keyword = input("Enter a keyword to search (name or accessibility): ")
    cursor.execute("SELECT * FROM locations WHERE name LIKE ? OR accessibility LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    if rows:
        print("\nSearch Results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Latitude: {row[2]}, Longitude: {row[3]}, Accessibility: {row[4]}")
    else:
        print("\nNo matching locations found.")

def generate_map():
    cursor.execute("SELECT * FROM locations")
    rows = cursor.fetchall()
    if rows:
        m = folium.Map(location=[0, 0], zoom_start=2)
        for row in rows:
            folium.Marker(
                location=[row[2], row[3]],
                popup=f"Name: {row[1]}\nAccessibility: {row[4]}",
            ).add_to(m)
        map_file = "accessibility_map.html"
        m.save(map_file)
        print(f"Map generated successfully! Open {map_file} to view it.")
    else:
        print("No locations to map.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add Location")
        print("2. View Locations")
        print("3. Search Locations")
        print("4. Delete Location")  # Delete option added to the menu
        print("5. Generate Accessibility Map")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_location()
        elif choice == "2":
            view_locations()
        elif choice == "3":
            search_locations()
        elif choice == "4":
            delete_location()
        elif choice == "5":
            generate_map()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()

# Close the connection when the program ends
conn.close()
