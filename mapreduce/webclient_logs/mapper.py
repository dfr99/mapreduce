#!/usr/bin/env python


import os
import sys


ps_objects_counter = 0
# Obtain file name and format it to get user name
file_path = os.environ['mapreduce_map_input_file']
processed_file_path = file_path.split('/')
file_name = processed_file_path[-1].split('.')[0].replace('con', '')


# input comes from STDIN (standard input)
for request in sys.stdin:
    # remove leading and trailing whitespace
    # split the request into the different request parameters
    parameters = request.strip().split()

    # Access to the request url
    url = str(parameters[3])
    # Count each access to an url made by a request
    print('%s\t%s' % (url, 1))

    # Access to the object extension extracted
    # from the url using list comprehension
    # Checking if the accessed object is a .ps file
    # If file was .ps extension, increment .ps files accessed by the user
    # Each file only contains requests from only one user
    if (url[-4:] == '.ps"'):
        ps_objects_counter += 1


# printing the count of .ps files accessed by each user
print('%s\t%s' % (file_name, ps_objects_counter))
