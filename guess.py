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
values = deque(maxlen=10)

# Read values from standard input
first_input = True  # Flag to check if it's the first input
for line in sys.stdin:
    # Strip whitespace and check if the line is not empty
    line = line.strip()
    if line:
        value = int(line)

        # Create a temporary list with the current values plus the new input
        temp_values = list(values) + [value]
        
        # Replace outliers in the temporary list
        adjusted_values = replace_outliers(temp_values)
        adjusted_value = adjusted_values[-1]  # Get the last value (the current input)

        # Add the adjusted value to the deque
        values.append(adjusted_value)

        if first_input:
            # For the first input, set a default range
            lower_bound = adjusted_value - 10  # Example: 10 units below the first input
            upper_bound = adjusted_value + 10  # Example: 10 units above the first input
            print(f"{lower_bound} {upper_bound}")
            first_input = False  # Set the flag to False after the first input
        else:
            # Ensure we have at least 2 values to calculate standard deviation
            if len(values) > 1:
                # Calculate the mean and standard deviation of the adjusted window
                mean = statistics.mean(values)
                std_dev = statistics.stdev(values)

                # Calculate the lower and upper bounds
                lower_bound = mean - 1.8 * std_dev
                upper_bound = mean + 1.8 * std_dev

                # Print the range for the next input
                print(f"{lower_bound:.0f} {upper_bound:.0f}")
            else:
                # If there's not enough data after filtering, print a message
                print("Not enough data to calculate range after replacing outliers.")
