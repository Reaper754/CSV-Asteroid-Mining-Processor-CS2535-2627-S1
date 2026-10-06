import csv

ore_points = 2
gas_points = 3
crystal_points = 5

ore_score = 0
gas_score = 0
crystal_score = 0
temp = 0

with open("input_asteroid_data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        try:
            temp = int(row[1])
            print(temp)
            ore_score = temp * ore_points
            print(ore_score)

        except TypeError:
            print("")
