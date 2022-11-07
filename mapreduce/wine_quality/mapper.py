#!/usr/bin/env python
import sys
from operator import add

is_first_line = True


for line in sys.stdin:
    # skip the first line (the header)
    if is_first_line:
        is_first_line = False
        keys = line.strip("\n").split(";")
        result = [0] * len(keys)
    else:
        float_line = [float(x) for x in line.split(";")]
        # i = 0
        # while i < len(keys):
            # print("%s\t%.4f" % (keys[i], float_line[i]))
            # i += 1
        result = list(map(add, result, float_line))


i = 0
while i < len(keys):
    print("%s\t%.4f" % (keys[i], result[i]))
    i += 1
