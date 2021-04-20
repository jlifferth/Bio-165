# We are looking for lines that have “PASS” in the 7th column. Remember that header lines start with “#”. Find all the
# # meta-data lines, the header line, and all the variant lines that have the word “PASS” in the 7th column. You are only
# # looking for “PASS” in the 7th column for variant lines and will keep all meta-data lines and the header line,
# # regardless of their content. Print all of these lines to the screen. Pass may show up in other columns, but when in
# # the 7th column it will appear alone and in all caps. Do not use regular expressions to do this. Remember, these files
# # are tab delimited ("backslash t").
#
#! /usr/bin/env

import sys

file_path = str(sys.argv[1])

with open(file_path) as my_file:
    in_file_variants = [] #
    for line in my_file:
        line = line.strip()
        if '#' in line: # all lines beginning with # are meta-data lines or header, these should be printed
            print(line)
        if '#' not in line: # all lines without # are variant lines, these are the lines that should be searched
            in_file_variants.append(line)
    filter_column = []
    for variant_line in in_file_variants:
        fields = variant_line.split('\t')
        for field in fields:
            field = field.strip()
        if len(fields) >= 7:
            if 'PASS' in fields[6]:
                print(variant_line)
