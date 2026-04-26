import os
import sqlite3
import random
import matplotlib.pyplot as plt

"""Simple population simulation and plotting utility.

This script creates a small SQLite database of city populations (base year
2025), optionally simulates yearly growth/decline for a number of years,
and provides functions to query and plot the simulated population history.
"""

def get_db_path() -> str:
	# Build a path to the database file sitting one directory above this file
	root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
	return os.path.join(root, "population_MO.db")

def create_db_and_insert_initial(db_path: str):
	cities_2025 = {
		"Miami": 470000,
		"Jacksonville": 985000,
		"Tampa": 410000,
		"Orlando": 320000,
		"St. Petersburg": 265000,
		"Hialeah": 240000,
		"Tallahassee": 200000,
		"Port St. Lucie": 258000,
		"Cape Coral": 230000,
		"Fort Lauderdale": 190000,
	}

	# Create DB (if missing) and ensure `population` table exists
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute(
		"""
		CREATE TABLE IF NOT EXISTS population(
			city TEXT,
			year INTEGER,
			population INTEGER,
			PRIMARY KEY(city, year)
		)
		"""
	)

	# Insert 2025 baseline populations (or replace if an entry already exists)
	for city, pop in cities_2025.items():
		cur.execute(
			"INSERT OR REPLACE INTO population(city, year, population) VALUES(?, ?, ?)",
			(city, 2025, int(pop)),
		)

	conn.commit()
	conn.close()

def simulate_population_growth(db_path: str, years: int = 20) -> None:
	"""Simulate population changes for each city for `years` years.

	The simulation applies a random yearly rate between -2% and +3%.
	"""

	conn = sqlite3.connect(db_path)
	cur = conn.cursor()

	# Find all cities present in the DB
	cur.execute("SELECT DISTINCT city FROM population")
	cities = [row[0] for row in cur.fetchall()]

	for city in cities:
		# Start from the 2025 baseline if present
		cur.execute(
			"SELECT population FROM population WHERE city = ? AND year = ?", (city, 2025)
		)
		row = cur.fetchone()
		if not row:
			# Skip cities that don't have a baseline year
			continue
		pop = int(row[0])
		year = 2025
		for i in range(1, years + 1):
			year += 1
			# yearly rate varies between -2% decline and +3% growth
			rate = random.uniform(-0.02, 0.03)
			pop = max(0, int(pop * (1 + rate)))
			cur.execute(
				"INSERT OR REPLACE INTO population(city, year, population) VALUES(?, ?, ?)",
				(city, year, pop),
			)

	conn.commit()
	conn.close()

def get_cities(db_path: str):
	# Return a sorted list of distinct city names in the DB
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute("SELECT DISTINCT city FROM population ORDER BY city")
	cities = [r[0] for r in cur.fetchall()]
	conn.close()
	return cities

def fetch_population_for_city(db_path: str, city: str):
	# Fetch (year, population) tuples for the given city ordered by year
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute(
		"SELECT year, population FROM population WHERE city = ? ORDER BY year", (city,)
	)
	rows = cur.fetchall()
	conn.close()
	return [(int(y), int(p)) for (y, p) in rows]

def plot_city_population(db_path: str, city: str) -> None:
	data = fetch_population_for_city(db_path, city)
	if not data:
		print(f"No data found for {city}.")
		return
	years, pops = zip(*data)
	plt.figure(figsize=(10, 5))
	plt.plot(years, pops, marker="o")
	plt.title(f"Population for {city} ({years[0]}-{years[-1]})")
	plt.xlabel("Year")
	plt.ylabel("Population")
	plt.grid(True)
	plt.tight_layout()
	plt.show()

def main() -> None:
	db_path = get_db_path()
	create_db_and_insert_initial(db_path)
	# Run the simulation for 20 years
	simulate_population_growth(db_path, years=20)

	cities = get_cities(db_path)
	print("Choose a city to display population growth (options):")
	for i, c in enumerate(cities, start=1):
		print(f"{i}. {c}")

	# Simple numeric menu selection for the user
	choice = int(input("Enter number of the city: "))
	if 1 <= choice <= len(cities):
		selected = cities[choice - 1]
		plot_city_population(db_path, selected)
	else:
		print("Invalid choice.")

if __name__ == "__main__":
	main()
