#!/usr/bin/env python


# Hadoop framework ensures that all values associated
# with the same key are processed by the same reducer
# Also, values are sorted alfabetically


import sys


count = 0.0
current_count = 0
current_wine = None
total = 0.0
wine = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    # parse the input we got from mapper
    wine, value = line.strip().split('\t', 1)

    try:
        # convert value (currently a string) to float
        value = float(value)
    except ValueError:
        # value was not a float, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: wine_characteristic) before it is passed to the reducer
    if current_wine == wine:
        total += value
        count += 1.0
    else:
        if current_wine:
            # write result to STDOUT
            print('%s\t%s' % (current_wine, total/count))

        current_wine = wine
        total = value
        count = 1.0

# Print last line
if current_wine == wine:
    print('%s\t%s' % (current_wine, total/count))
