"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""
import sys

def get_reverse(seq):
    """ Returns a reverse copy of the DNA string. """
    return seq[::-1]

def get_complement(seq):
    """ Returns a complementt of the DNA string. """
    DNA_complement_map = dict(A='T', T='A', C='G', G='C')
    complement = ''
    for base in seq:
        complement += DNA_complement_map[base]
    return complement

def get_reverse_complement(finput):
    """ Returns a reverse complement of the DNA string. """
    with open(finput, 'r') as fh:
        seq = fh.readline().strip()
    fh.close()
    return get_complement(get_reverse(seq))

if __name__ == '__main__':
    result = get_reverse_complement(sys.argv[1])
    print(result)
