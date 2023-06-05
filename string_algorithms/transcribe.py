"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
import sys
from time import time

def transcribe(finput):
    """ Returns the transcribed RNA string for a DNA sequence. """
    with open(finput, 'r') as fh:
        seq = fh.readline().strip()
    fh.close()
    rna = ''
    for base in seq:
        if base == 'T':
            rna += 'U'
        else:
            rna += base
    return rna

# runs 100% faster when measured in 10000 iterations
def short_transcribe(finput):
    with open(finput, 'r') as fh:
        seq = fh.readline().strip()
    fh.close()
    return seq.replace('T', 'U')

if __name__ == '__main__':
    result = short_transcribe(sys.argv[1])
    print(result)
