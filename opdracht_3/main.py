import sqlite3

DATABASE_PATH = "opdracht_3/travel_db.db"

def getAllCars():
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM cars")
	cars = cursor.fetchall()

	conn.close()

	return cars

def getAllDestinations():
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute("SELECT name, distance FROM destinations")
	destinations = cursor.fetchall()

	conn.close()

	return destinations

def getDestinationDistance(name):
	destination = list(filter(lambda dest: dest[0] == name, getAllDestinations()))

	if len(destination) < 1:
		return None
	
	return destination[0][1]

def isCarCapable(kilometersPerLiter, fuelCapacity, distance):
	kmPerCycle = kilometersPerLiter * fuelCapacity

	return kmPerCycle > distance

def	getCapableCars(destinationName: str) -> list:
	destinationDistance = getDestinationDistance(destinationName)

	if not destinationDistance:
		return []

	cars = getAllCars()
	capableCars = list(filter(lambda car: isCarCapable(car[3], car[4], destinationDistance), cars))

	return capableCars

for destination in (("A", 0), ("B", 0), ("C", 0), *getAllDestinations()):
	cars = getCapableCars(destination[0])

	print(f"\n{destination[0]} - {destination[1]} km")

	if len(cars) > 0:
		for car in cars:
			print(f"{car[1]} {car[2]}")
	else:
		print("Geen geschikte auto's gevonden")

# Test
print("\n")

result = [(1, 'Toyota', 'Corolla', 15.0, 50.0), (2, 'Honda', 'Civic', 14.5, 47.0), (3, 'Ford', 'Mustang', 8.3, 60.0), (4, 'Chevrolet', 'Impala', 10.0, 65.0), (5, 'BMW', 'X5', 9.4, 85.0), (6, 'Audi', 'A4', 14.0, 60.0), (7, 'Mercedes-Benz', 'C-Class', 13.5, 66.0), (8, 'Volkswagen', 'Golf', 16.0, 55.0), (9, 'Hyundai', 'Elantra', 15.5, 53.0), (10, 'Nissan', 'Altima', 13.0, 56.0), (11, 'Toyota', 'Corolla', 15.0, 50.0), (12, 'Honda', 'Civic', 14.5, 47.0), (13, 'Ford', 'Mustang', 8.3, 60.0), (14, 'Chevrolet', 'Impala', 10.0, 65.0), (15, 'BMW', 'X5', 9.4, 85.0), (16, 'Audi', 'A4', 14.0, 60.0), (17, 'Mercedes-Benz', 'C-Class', 13.5, 66.0), (18, 'Volkswagen', 'Golf', 16.0, 55.0), (19, 'Hyundai', 'Elantra', 15.5, 53.0), (20, 'Nissan', 'Altima', 13.0, 56.0)]
test = getCapableCars("Tunis")
print("Tunis", result == test)

result = [(1, 'Toyota', 'Corolla', 15.0, 50.0), (2, 'Honda', 'Civic', 14.5, 47.0), (4, 'Chevrolet', 'Impala', 10.0, 65.0), (5, 'BMW', 'X5', 9.4, 85.0), (6, 'Audi', 'A4', 14.0, 60.0), (7, 'Mercedes-Benz', 'C-Class', 13.5, 66.0), (8, 'Volkswagen', 'Golf', 16.0, 55.0), (9, 'Hyundai', 'Elantra', 15.5, 53.0), (10, 'Nissan', 'Altima', 13.0, 56.0), (11, 'Toyota', 'Corolla', 15.0, 50.0), (12, 'Honda', 'Civic', 14.5, 47.0), (14, 'Chevrolet', 'Impala', 10.0, 65.0), (15, 'BMW', 'X5', 9.4, 85.0), (16, 'Audi', 'A4', 14.0, 60.0), (17, 'Mercedes-Benz', 'C-Class', 13.5, 66.0), (18, 'Volkswagen', 'Golf', 16.0, 55.0), (19, 'Hyundai', 'Elantra', 15.5, 53.0), (20, 'Nissan', 'Altima', 13.0, 56.0)]
test = getCapableCars("Tripoli")
print("Tripoli", result == test)

result = []
test = getCapableCars("Cairo")
print("Cairo", result == test)

result = []
test = getCapableCars("Bamako")
print("Bamako", result == test)

result = []
test = getCapableCars("Khartoum")
print("Khartoum", result == test)