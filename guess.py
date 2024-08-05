import sys
from collections import deque
import statistics

# Initialize the deque with a maximum length of 10
values = deque(maxlen=10)

# Read values from standard input
first_input = True  # Flag to check if it's the first input
for line in sys.stdin:
    # Strip whitespace and check if the line is not empty
    line = line.strip()
    if line:
        value = int(line)
        values.append(value)

        if first_input:
            # For the first input, set a default range
            lower_bound = value - 10  # Example: 10 units below the first input
            upper_bound = value + 10  # Example: 10 units above the first input
            print(f"{lower_bound} {upper_bound}")
            first_input = False  # Set the flag to False after the first input
        else:
            # Ensure we have at least 2 values to calculate standard deviation
            if len(values) > 1:
                # Calculate the mean and standard deviation of the current window
                mean = statistics.mean(values)
                std_dev = statistics.stdev(values)

                # Calculate the lower and upper bounds
                lower_bound = mean - 1.8 * std_dev
                upper_bound = mean + 1.8 * std_dev

                # Print the range for the next input
                print(f"{lower_bound:.0f} {upper_bound:.0f}")
            else:
                # If there's only one value, we can't calculate a range
                print("Not enough data to calculate range.")
