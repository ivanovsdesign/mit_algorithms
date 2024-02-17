# Comparison of running times

import math

# 1000000 microseconds in a second
interval = 1000000


# -------------------
# n lg(n)

n = 1 

while n * math.log2(n) < interval:
    n += 1

print(f'Minimum value of n * log(n) = {n-1}')

# -------------------
# n!

n = 1

while math.factorial(n) < 1000000:
    n += 1

print(f'Minimum value of n!: {n - 1}')