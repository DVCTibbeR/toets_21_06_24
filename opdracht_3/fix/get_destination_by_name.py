import sqlite3

def get_destination(destination_name):

    conn = sqlite3.connect('opdracht_3/travel_db.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM destinations WHERE name = ?', (destination_name,))
    destination = cursor.fetchone()

    conn.close()

    return destination

destination_name = 'Cairo'
destination = get_destination(destination_name)
if destination:
    print(f"ID: {destination[0]}, Name: {destination[1]}, Distance: {destination[2]} km")
else:
    print(f"Destination '{destination_name}' not found.")
