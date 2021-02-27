import sys

file_path = str(sys.argv[1])

def writeToFile(line_in):
    in_file_variants = []
    if line_in[0] == '#':  # all lines beginning with # are meta-data lines or header, these should be printed
        print(line.strip(), end='\n')
    if line_in[0] != '#':  # all lines without # are variant lines, these are the lines that should be searched
        in_file_variants.append(line_in)
    for variant_line in in_file_variants:
        fields = variant_line.split('\t')
        if len(fields) >= 7:
            print(fields)
            if 'PASS' in fields[6]:
                print(variant_line.strip(), end= '\n')

with open(file_path) as my_file:
    for line in my_file:
        writeToFile(line)
