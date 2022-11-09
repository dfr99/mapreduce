#!/usr/bin/env python


import os
import sys


iterator = 0
names = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]


# Obtain file name and format it to retrieve the type of wine
file_path = os.environ['mapreduce_map_input_file']
wine = file_path.split('/')[-1].split('-')[1].split('.')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    # split the line into the different values
    values = line.strip().split(';')

    # we skip the line containing strings
    if '"fixed acidity"' in values:
        continue

    for value in values:
        print('%s\t%s' % (wine + ' ' + names[iterator], value))
        iterator += 1

    iterator = 0
