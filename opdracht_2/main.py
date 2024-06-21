from math import ceil
from random import randint

def getAmountFuelStops(kilometersPerLiter, fuelCapacity, kilometersLeft):
	kmPerCycle = fuelCapacity * kilometersPerLiter

	return ceil(kilometersLeft / kmPerCycle) - 1

# Test
test = getAmountFuelStops(1, 1, 10)
print([1, 1, 10], 9, test == 9)

test = getAmountFuelStops(10, 1, 10)
print([10, 1, 10], 0, test == 0)

test = getAmountFuelStops(30, 10, 230)
print([30, 10, 230], 0, test == 0)

test = getAmountFuelStops(20, 10, 230)
print([30, 10, 230], 1, test == 1)