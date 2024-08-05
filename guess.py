import sys
from collections import deque
import statistics

# Initialize the deque with a maximum length of 10
values = deque(maxlen=10)

# Read values from standard input
for line in sys.stdin:
    # Strip whitespace and check if the line is not empty
    line = line.strip()
    if line:
        value = int(line)
        values.append(value)
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
