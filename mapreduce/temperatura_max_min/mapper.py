#!/usr/bin/env python
import sys


# input from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespaces
    # split lines using whitespaces as separator
    process_line = line.strip().split(" ")

    # remove whitespaces process_line list items
    removed_whitespaces_line = [item for item in process_line if item != '']

    # avoid invalid or miss values
    if removed_whitespaces_line[5] not in ['-9999.0', '-99.000', '-9999.00'] and removed_whitespaces_line[6] not in ['-9999.0', '-99.000', '-9999.00']:
        # print city code, max and min temperatures
        print("%s\t%s\t%s" % (removed_whitespaces_line[0], removed_whitespaces_line[5], removed_whitespaces_line[6]))
