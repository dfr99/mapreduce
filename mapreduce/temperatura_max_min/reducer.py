#!/usr/bin/env python
import sys

# Nota: el framework de hadoop garantiza que todos los
# valores asociados con la misma clave (palabra) van al mismo reducer

max_temperature = 0
max_temperature_code = None
min_temperature = 0
min_temperature_code = None


# input from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    # split line using tab as separator
    code, current_max, current_min = line.strip().split("\t", 2)

    # Convert temperatures to float
    try:
        max_tmp = float(current_max)
    except ValueError:
        continue
    try:
        min_tmp = float(current_min)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: code) before it is passed to the reducer
    if (max_temperature < max_tmp) and (max_tmp > 27.0):
        max_temperature = max_tmp
        max_temperature_code = code
    if (min_temperature > min_tmp) and (min_tmp < -1.0):
        min_temperature = min_tmp
        min_temperature_code = code

print("Min\t%s\t%s" % (min_temperature_code, min_temperature))
print("Max\t%s\t%s" % (max_temperature_code, max_temperature))
