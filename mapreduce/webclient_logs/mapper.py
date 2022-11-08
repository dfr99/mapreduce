#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # file_name = os.environ['mapreduce_map_input_file']

    # us = file_name.split('/')
    # user = us[-1].split(".")[0][3:]

    process_line = line.strip().split()
    # increase counters
    if process_line[3].split('.')[-1] == 'ps"':
        # Print user and 1 that represent a access to file with .ps
        # print('%s\t%s' % (user, 1))
        # Print the URL and 1
        print('%s\t%s' % (process_line[3], 1))
