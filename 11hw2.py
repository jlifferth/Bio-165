#! /usr/bin/env python3

import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path) as in_file, open(output_path, 'w') as out_file:
        sequence_line = ''
        for line in in_file:
                if line[0] == '>':
                        if sequence_line != '':
                                out_file.write(sequence_line.strip() + '\n')
                        line = line.strip()
                        out_file.write(line + '\n')
                        sequence_line = ''
                else:
                        line = line.upper()
                        sequence_line += line.strip()
        out_file.write(sequence_line.strip() + '\n')