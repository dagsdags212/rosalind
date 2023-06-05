"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

import sys

def count_nucleotides(finput):
    """ Returns the counts of each nucleotide in the given DNA string. """
    with open(finput, 'r') as fh:
        seq = fh.readline().strip()
    fh.close()

    counts = {base: 0 for base in 'ACGT'}
    for base in seq:
        counts[base] += 1
    return list(counts.values())

if __name__ == '__main__':
    result = count_nucleotides(sys.argv[1])
    print(*result)
