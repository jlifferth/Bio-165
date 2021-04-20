#! /usr/bin/env python3

import sys

read_path = sys.argv[1]
write_path = sys.argv[2]

with open(read_path) as in_file, open(write_path, 'w') as out_file:
        for line in in_file:
                line = line.strip()
                fields = line.split('\t')
                line_sum = int(fields[0]) + int(fields[1])
                out_file.write(fields[0] + ' + ' + fields[1] + ' = ' + str(line_sum) + '\n')
                                                                          
