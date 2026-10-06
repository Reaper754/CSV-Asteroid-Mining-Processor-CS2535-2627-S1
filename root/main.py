import csv

ore_points = 2
gas_points = 3
crystal_points = 5

with open("input_asteroid_data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)


with open("output_asteroid_data.csv", "w", newline="") as file:
    headers = ["astroid_id", "ore_units", "crystal_units", "gas_units", "total_units", "cargo_value"]
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in data:
        try:
            total_units = int(row[1]) + int(row[3]) + int(row[2])
            ore_score = int(row[1]) * ore_points
            gas_score = int(row[3]) * gas_points
            crystal_score = int(row[2]) * crystal_points
            cargo_value = ore_score + gas_score + crystal_score
            writer.writerow([row[0], row[1], row[2], row[3], total_units, cargo_value])
        except ValueError:
            pass

