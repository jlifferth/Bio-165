# 6. Split One List into Two Lists with a For Loop
#
# System arguments are stored as a list. Given an unknown number of system arguments, split the list of system
# arguments into two different lists: one that has the even numbers and one that has the odd numbers. Print the list
# with even numbers in ascending order on one line and the list with odd numbers in ascending order on the next line.
# Just print the lists (no special formatting). You must use a for loop.
#
# We will run your code with the following commands:
#
# python studentcode.py 1 4 2 90 5 3 9
# python studentcode.py 903 901 109283 121 1
#
# The expected output for this program would be:
#
# [2, 4, 90]
# [1, 3, 5, 9]
# []
# [1, 121, 901, 903, 109283]

#! /usr/bin/env python3

import sys
system_nums = sys.argv[1:]
# seq = input("Input : ")

all_numbers = []
for argument in system_nums:
    all_numbers.append(int(argument))
# print('sequences = ' + str(sequences))

even = []
odd = []
for number in all_numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
even.sort()
odd.sort()
print(even)
print(odd)
