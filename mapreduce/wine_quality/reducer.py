#!/usr/bin/env python
import sys
from functools import reduce

file_lines = 1599
keys = []
sums = []


for line in sys.stdin:
    line_array = line.strip("\n").split("\t")
    # result = reduce(lambda x: x / len(line_array[1].split(","), line_array[1].split(",")))
    # print(line_array[0], result)
    keys.append(line_array[0])
    sums.append(float(line_array[1]))

reduce_res = list(map(lambda x: x / file_lines, sums))


i = 0
while i < len(keys):
    print("%s\t%.4f" % (keys[i], reduce_res[i]))
    i += 1
