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
