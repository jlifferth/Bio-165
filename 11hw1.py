#! /usr/bin/env python3

import sys
import re

file_path = sys.argv[1]
output_path = sys.argv[2]

with open(file_path) as my_file, open(output_path, 'w') as out_file:
        variant_lines = []
        for line in my_file:
                if line[0] == '#':
                        out_file.write(line)
                        print(line.strip())
                else:
                        variant_lines.append(line)
        for variant_line in variant_lines:
                fields = variant_line.split('\t')
                if fields[6] == 'PASS':
                        Regex = r'PASS'
                        Replace = r'pass'
                        new_variant_line = re.sub(Regex, Replace, variant_line)
                        out_file.write(new_variant_line)

