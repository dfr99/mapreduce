#!/usr/bin/env python
import sys
from functools import reduce

keys = []
sums = []

red_lines = 1599
white_lines = 4598

for line in sys.stdin:
    line_array = line.strip("").split("\t")
    if line_array[0] == "red":
        print("%s\t%s\t%s" % (line_array[0], line_array[1], float(line_array[2]) / red_lines))
    elif line_array[0] == "white":
        print("%s\t%s\t%s" % (line_array[0], line_array[1], float(line_array[2]) / white_lines))
