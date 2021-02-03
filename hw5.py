# 5. Alphabetize DNA with a While Loop
#
# Your code will accept an unknown number of system arguments, each of which will be a DNA sequence. Convert the DNA sequences to uppercase using a while loop. Print the alphabetized list of sequences as a list. Your program should handle a mix of upper/lower case letters. You must use a while loop. You cannot use string.upper().
#
# We will test your code with the following commands:
#
# python studentcode.py A a t C g AA gG c AG T TA a G aaaa
# python studentcode.py c AAaattTTccCCggGGaAcCtTgG g
#
# The expected output from your program is:
#
# ['A', 'A', 'A', 'AA', 'AAAA', 'AG', 'C', 'C', 'G', 'G', 'GG', 'T', 'T', 'TA']
# ['AAAATTTTCCCCGGGGAACCTTGG', 'C', 'G']

#! /usr/bin/env python3

import sys
system_seqs = sys.argv[1:]
# seq = input("Input : ")

sequences = []
for sequence in system_seqs:
    sequences.append(sequence)
# print('sequences = ' + str(sequences))

sequences_upper = []
index = 0
while index < len(sequences):
    sequences[index] = sequences[index].replace('a', 'A')
    sequences[index] = sequences[index].replace('g', 'G')
    sequences[index] = sequences[index].replace('c', 'C')
    sequences[index] = sequences[index].replace('t', 'T')
    sequences_upper.append(sequences[index])
    index += 1
sequences_upper.sort()
print("sequences_upper =" + str(sequences_upper))
