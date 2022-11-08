#!/usr/bin/env python

import sys
from operator import add


is_first_line = True
wine = "red"


for line in sys.stdin:
    # skip the first line (the header)
    if is_first_line:
        is_first_line = False
        keys = line.strip().split(";")
        result = [0] * len(keys)
    else:
        try:
            float_line = [float(x) for x in line.split(";")]
        except ValueError:
            i = 0
            # Print red wine data
            while i < len(keys):
                print("%s\t%s\t%.4f" % (wine, keys[i], result[i]))
                i += 1
            wine = "white"
            result = [0] * len(keys)
        result = list(map(add, result, float_line))


# Print white wine data
i = 0
while i < len(keys):
    print("%s\t%s\t%.4f" % (wine, keys[i], result[i]))
    i += 1
