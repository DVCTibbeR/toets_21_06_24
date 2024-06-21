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
 
# Test
for destination in (("A", 0), ("B", 0), ("C", 0), *getAllDestinations()):
	cars = getCapableCars(destination[0])

	print(f"\n{destination[0]} - {destination[1]} km")

	if len(cars) > 0:
		for car in cars:
			print(f"{car[1]} {car[2]}")
	else:
		print("Geen geschikte auto's gevonden")