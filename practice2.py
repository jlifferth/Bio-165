#! /usr/bin/env

import sys

total_sum = 0
file_path = str(sys.argv[1])
with open(file_path) as my_file:
    for line in my_file:
        total_sum += int(line)
print(total_sum)
