#Using math module and the variables a=2, b=5, z=90,
#perform mathematical operations:
# - square root(a^2+3*b^2) + 15;
# - cosine of 120 degrees;
# - sine of 90 degrees,
# - sine from the value in radians 2*pi

import math

a = 2
b = 5
z = 90

print(round(math.sqrt((a^2+3*b^2) + 15), 2))
print(round(math.cos(math.radians(120)), 2))
print(math.sin(math.radians(z)))
print(round(math.sin(2*math.pi)))