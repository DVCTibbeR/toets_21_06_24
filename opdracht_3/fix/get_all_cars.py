import sqlite3

def get_all_cars():
    conn = sqlite3.connect('opdracht_3/travel_db.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()

    conn.close()

    return cars

all_cars = get_all_cars()

for car in all_cars:
    print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Usage: {car[3]} km/l, Tank Volume: {car[4]} liters")
