import sqlite3

def add_location():
    name = input("Enter location name: ")
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    features = input("Enter accessibility features (comma-separated): ")
    
    try:
        conn = sqlite3.connect('accessibility.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO locations (name, latitude, longitude, accessibility_features) VALUES (?, ?, ?, ?)", 
                       (name, latitude, longitude, features))
        conn.commit()
        print("Location added successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_locations():
    try:
        conn = sqlite3.connect('accessibility.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM locations")
        locations = cursor.fetchall()
        print("\nLocations:")
        for location in locations:
            print(location)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def delete_location():
    location_id = int(input("Enter the ID of the location to delete: "))
    try:
        conn = sqlite3.connect('accessibility.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM locations WHERE id = ?", (location_id,))
        conn.commit()
        print("Location deleted successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Location")
        print("2. View Locations")
        print("3. Delete Location")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_location()
        elif choice == "2":
            view_locations()
        elif choice == "3":
            delete_location()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
