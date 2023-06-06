"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order
"""
import sys
from reverse_complement import get_reverse, get_complement
import parse_fasta as pf

def is_reverse_palindrome(seq):
    return seq == get_complement(get_reverse(seq))

def find_reverse_palindromes(seq):
    # get all substrings of seq with length values between 4 and 12, inclusive
    valid_substrings = []
    for i in range(4, 13):
        for j in range(0, len(seq)-i+1):
            substr = seq[j:j+i]
            # add substring and index + 1 if current sub is a reverse palindrome
            if is_reverse_palindrome(substr):
                valid_substrings.append((j+1, len(substr)))

    return sorted(valid_substrings, key=lambda x: x[0])

if __name__ == "__main__":
    if '\\' in sys.argv[1]:
        path = sys.argv[1]
        ids, seqs = pf.extract_seqs_from_fasta(path)
        result = find_reverse_palindromes(seqs[0])
    else:
        result = find_reverse_palindromes(sys.argv[1])
    for tuple in result:
        print(*tuple)
