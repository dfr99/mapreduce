#!/usr/bin/env python

# Hadoop framework ensures that all values associated
# with the same key are processed by the same reducer
# Also, values are sorted alfabetically


import sys


current_url_or_user_id = None
max_user = ''
max_url = ''
url_or_user_id = None

max_user_count = 0
max_url_count = 0
current_count = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    url_or_user_id, count = line.split('\t', 1)
    try:
        # try to convert count (currently a string) to int
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: url_or_user_id) before it is passed to the reducer
    # Accumulate data from the same key. When the key changes, keep their
    # values as a new maximums if they exceeds the current maximum.
    if current_url_or_user_id == url_or_user_id:
        current_count += count
    else:
        if current_url_or_user_id and current_url_or_user_id is not None:
            if '://' in current_url_or_user_id:
                if (current_count > max_url_count):
                    max_url = current_url_or_user_id
                    max_url_count = current_count
            elif (current_count > max_user_count):
                max_user = current_url_or_user_id
                max_user_count = current_count

        current_count = count
        current_url_or_user_id = url_or_user_id


# Last iteration to check the last user/url and its counter
if current_url_or_user_id == url_or_user_id:
    if '://' in current_url_or_user_id:
        if (current_count > max_url_count):
            max_url = current_url_or_user_id
            max_url_count = current_count
    elif (current_count > max_user_count):
        max_user = current_url_or_user_id
        max_user_count = current_count


# write result to STDOUT
print('%s\t%s' % (max_user, max_user_count))
print('%s\t%s' % (max_url, max_url_count))
