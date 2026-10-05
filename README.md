# CSV Asteroid Mining Processor


# Asteroid Mining Data Processor

Create a Python program in `main.py` that processes data collected from asteroid mining scans. Each row of the provided CSV file contains the amount of three different resources found on an asteroid. Your program will read the existing data, calculate new numerical values for every asteroid, and write the processed results to a **new CSV file**.

Each resource has a different cargo value:

- Ore is worth **2 points per unit**
- Crystal is worth **5 points per unit**
- Gas is worth **3 points per unit**

For each asteroid:

```text
total_units = ore_units + crystal_units + gas_units

cargo_value = (ore_units × 2) + (crystal_units × 5) + (gas_units × 3)
```

For example, the first asteroid begins with:

```text
AST-001,42,18,27
```

Its processed values should be:

```text
total_units = 87
cargo_value = 255
```

## Requirements

* [ ] Use Python's `csv` module to read the provided `input_asteroid_data.csv` file and process each asteroid row.
* [ ] Use the existing CSV headers to access `asteroid_id`, `ore_units`, `crystal_units`, and `gas_units`.
* [ ] Convert the three resource values from strings into integers before performing calculations.
* [ ] Calculate `total_units` for every asteroid by adding its ore, crystal, and gas units together.
* [ ] Calculate `cargo_value` for every asteroid using the resource point values provided above.
* [ ] Add the calculated `total_units` and `cargo_value` values to each asteroid's processed data.
* [ ] Write the processed data to a **new file named `output_asteroid_data.csv`**. Do not modify or overwrite the original `input_asteroid_data.csv` file.
* [ ] Write the following headers to the new CSV file: `asteroid_id`, `ore_units`, `crystal_units`, `gas_units`, `total_units`, `cargo_value`.

The finished project should contain:

```text
main.py
input_asteroid_data.csv
output_asteroid_data.csv
```

The beginning of `output_asteroid_data.csv` should look similar to:

```csv
asteroid_id,ore_units,crystal_units,gas_units,total_units,cargo_value
AST-001,42,18,27,87,255
AST-002,15,33,21,69,258
```

## Assessment — 20 Marks

| Assessment Item | Criteria | Marks |
|---|---|---:|
| Reading CSV Data | Uses the `csv` module to read `asteroid_mining.csv` and processes each asteroid row. | 3 |
| Using Headers | Correctly accesses the existing data using the CSV headers. | 2 |
| Numeric Conversion | Converts the resource values into integers before performing calculations. | 2 |
| Total Units | Correctly calculates `total_units` for every asteroid. | 3 |
| Cargo Value | Correctly calculates `cargo_value` using the required resource values. | 4 |
| Updating Row Data | Adds both calculated values to the appropriate processed asteroid data. | 2 |
| Writing the Output File | Creates `asteroid_mining_processed.csv` and writes the processed asteroid data to it without overwriting the original input file. | 2 |
| Output Headers | Writes all six required headers to the processed CSV file. | 2 |
|  | **Total** | **20** |
