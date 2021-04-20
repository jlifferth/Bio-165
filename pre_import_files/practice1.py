# Write a program that accepts one parameter from the command line, the path to a file. Your program should count the
# number of characters, including end-of-line characters, number of characters excluding end-of-line characters, and
# lines in the file and print the numbers to the screen.
#! /usr/bin/env

import sys

file_path = str(sys.argv[1])

number_of_characters = 0
number_of_characters_stripped = 0
number_of_lines = 0
with open(file_path) as my_file:
    for line in my_file:
        number_of_characters += len(line)
        line = line.strip()
        number_of_characters_stripped += len(line)
        number_of_lines += 1
print(number_of_characters)
print(number_of_characters_stripped)
print(number_of_lines)
