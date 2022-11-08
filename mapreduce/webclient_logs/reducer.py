#!/usr/bin/env python

import sys

current_user = None
total_user = 0
user = None

for line in sys.stdin:

    line = line.strip()
    array = line.split('\t', 1)

    user = array[0]
    try:
        count = int(array[1])
    except ValueError:
        continue

    if current_user == user:
        total_user += count
    else:
        if current_user:
            print '%s\t%s' % (current_user, total_user)
        current_user = user
        total_user = count
if current_user == user:
    print '%s\t%s' % (current_user, total_user)
