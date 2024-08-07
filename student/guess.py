import sys
from collections import deque
import statistics

# Function to replace outliers with the median of non-outlier values
def replace_outliers(data, std_dev_factor=3):
    if len(data) < 2:  # Ensure enough data for calculation
        return data

    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)

    lower_bound = mean - std_dev_factor * std_dev
    upper_bound = mean + std_dev_factor * std_dev

    non_outliers = [x for x in data if lower_bound <= x <= upper_bound]
    if non_outliers:
        median = statistics.median(non_outliers)
        return [median if x < lower_bound or x > upper_bound else x for x in data]
    else:
        return [mean] * len(data)

# Initialize deque for storing input values
values = deque(maxlen=50)
input_count = 0

# Read values from standard input
for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            value = int(line)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        values.append(value)
        input_count += 1

        if input_count > 1:  # Start calculations from second input onward
            adjusted_values = replace_outliers(list(values))

            if len(adjusted_values) > 1:  # Ensure enough data for statistical calculations
                mean = statistics.mean(adjusted_values)
                std_dev = statistics.stdev(adjusted_values)

                lower_bound = mean - 3 * std_dev
                upper_bound = mean + 3 * std_dev

                print(f"{lower_bound:.0f} {upper_bound:.0f}")
            else:
                print("Not enough data to calculate range after replacing outliers.")
