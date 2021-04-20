#! /usr/bin/env python3

import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path) as in_file, open(output_path, 'w') as out_file:
        for line in in_file:
                nucleotides = ''
                line = line.strip()
                if line[0] == '>':
                        out_file.write(line + '\n')
                        print(line)
                else:
                        for nucleotide in line:
                                if nucleotide != ' ':
                                        nucleotides += nucleotide
                        out_file.write(nucleotides + '\n')
                        print(nucleotides)
