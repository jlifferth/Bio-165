# 4. Alphabetize DNA with a For Loop
#
# Your code will accept an unknown number of system arguments, each of which will be a DNA sequence.
# Convert the DNA sequences to uppercase using a for loop. Print the alphabetized list of sequences
# as a list. Your program should handle a mix of upper/lower case letters. You must use a for loop.
# You cannot use string.upper().
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

nucleotides = []
for seq1 in system_seqs:
    nucleotides.append(seq1)
print('nucleotides = ' + str(nucleotides))

nucleotides.sort()
print('nucleotides = ' + str(nucleotides))

nucleotides_upper = []
for sequence in nucleotides:
    sequence = sequence.replace('a','A')
    sequence = sequence.replace('g', 'G')
    sequence = sequence.replace('c', 'C')
    sequence = sequence.replace('t', 'T')
    nucleotides_upper.append(sequence)
nucleotides_upper.sort()
print(nucleotides_upper)

# list_2 = []
# for seq2 in list_seqs:
#     for nucleotide in seq2:
#         if nucleotide == 'a' or nucleotide == 'A':
#             list_2.append('A')
#         elif nucleotide == 'g' or nucleotide == 'G':
#             list_2.append('G')
#         elif nucleotide == 'c' or nucleotide == 'C':
#             list_2.append('C')
#         elif nucleotide == 't' or nucleotide == 'T':
#             list_2.append('T')
# list_2.sort()
# print(list_2)




# if nucleotide == 'a':
#     nucleotide.replace('a','A')
# elif nucleotide == 'g':
#     nucleotide.replace('g','G')
# elif nucleotide == 'c':
#     nucleotide.replace('c','C')
# elif nucleotide == 't':
#     nucleotide.replace('t','T')
