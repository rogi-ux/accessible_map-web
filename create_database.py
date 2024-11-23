import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('accessibility.db')  # Create/access database
        cursor = conn.cursor()
        # Create the locations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                accessibility_features TEXT
            )
        ''')
        conn.commit()
        print("Database and table created successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
