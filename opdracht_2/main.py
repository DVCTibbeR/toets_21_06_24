from math import floor
from random import randint

def getAmountFuelStops(kilometersPerLiter, fuelCapacity, kilometersLeft):
	kmPerCycle = fuelCapacity * kilometersPerLiter

	return floor(kilometersLeft / kmPerCycle)

# Test
for _ in range(6):
	kmPerLiter = randint(5, 15)
	fuelCapacity = randint(10, 30)
	kmLeft = randint(25, 500)

	fuelStops = getAmountFuelStops(kmPerLiter, fuelCapacity, kmLeft)

	print(f"Als je nog {kmLeft} km moet rijden, er {fuelCapacity} liter in je tank past en je {kmPerLiter} km per liter kan rijden tank je onderweg {fuelStops} keer.")