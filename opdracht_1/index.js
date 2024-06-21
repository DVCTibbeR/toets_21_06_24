function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
	return kilometersNaarTankstation < (resterendeLiters * kilometersPerLiter);
}

// Test
function randomInt(min, max) {
	return Math.round(Math.random() * (max - min) + min);
}

for (let i = 0; i < 6; i++) {
	let [kmPump, kmLiter, liter] = [randomInt(25, 100), randomInt(5, 15), randomInt(5, 10)];
	let possible = kanBereikenTankstation(kmPump, kmLiter, liter) ? "wel" : "niet";

	console.log(`Het tankstation is ${kmPump} km van jou vandaan, met ${liter} liter in je tank en ${kmLiter} km/L kan je het tankstation ${possible} halen.`);
}