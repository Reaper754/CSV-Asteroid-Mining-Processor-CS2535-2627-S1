import csv

ore_points = 2
gas_points = 3
crystal_points = 5

with open("input_asteroid_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
