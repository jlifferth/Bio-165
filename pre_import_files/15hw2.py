import sys

input_path = str(sys.argv[1])
output_path = sys.argv[2]

def writeToFile(line_in):
        line_in = line_in.strip()
        if line_in[0] == '#':
            return True
        if line_in[0] != '#':
            fields = line_in.split('\t')
            if 'PASS' in fields[6]:
                return True
        else:
            return False

with open(input_path) as my_file, open(output_path,'w') as out_file:
    for line in my_file:
        if True:
            writeToFile(line)
            out_file.write(line)
        elif False:
            continue
