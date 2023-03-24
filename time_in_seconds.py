
import math
from cmath import pi
length = float(input("What is the length (meters): "))

time = 2 * pi * math.sqrt (length / 9.81)

print(f"Time in (seconds) is: {time:.1f} seconds.\n")