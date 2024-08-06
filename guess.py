import sys
from collections import deque
import statistics

# Function to replace outliers with the median of non-outlier values
def replace_outliers(data, std_dev_factor=3):
    if len(data) < 2:  # Not enough data to calculate mean and standard deviation
        return data

    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)

    lower_bound = mean - std_dev_factor * std_dev
    upper_bound = mean + std_dev_factor * std_dev

    # Replace outliers with the median of the non-outlier values
    non_outliers = [x for x in data if lower_bound <= x <= upper_bound]
    if non_outliers:  # Ensure there are non-outlier values to calculate the median
        median = statistics.median(non_outliers)
        return [median if x < lower_bound or x > upper_bound else x for x in data]
    else:
        return [mean] * len(data)  # If all values are outliers, replace with the mean

# Initialize the deque with a maximum length of 10
values = deque(maxlen=50)

# Read values from standard input
input_count = 0  # Count the number of inputs
for line in sys.stdin:
    # Strip whitespace and check if the line is not empty
    line = line.strip()
    if line:
        try:
            value = int(line)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        values.append(value)
        input_count += 1

        if input_count > 1:  # Start calculating the range from the second input onward
            # Replace outliers from the current values
            adjusted_values = replace_outliers(list(values))

            # Ensure we have at least 2 values to calculate standard deviation
            if len(adjusted_values) > 1:
                # Calculate the mean and standard deviation of the adjusted window
                mean = statistics.mean(adjusted_values)
                std_dev = statistics.stdev(adjusted_values)

                # Calculate the lower add upper bounds
                lower_bound = mean - 3 * std_dev
                upper_bound = mean + 3 * std_dev

                # Print the range for the next input
                print(f"{lower_bound:.0f} {upper_bound:.0f}")
            else:
                # If there's not enough data after filtering, print a message
                print("Not enough data to calculate range after replacing outliers.")
