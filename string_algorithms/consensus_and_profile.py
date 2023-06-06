"""
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the
intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in
the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol
having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""
import sys
from parse_fasta import extract_seqs_from_fasta

def generate_profile_matrix(collection):
    n = len(collection[0])
    m = len(collection)
    profile = {base: [0] * n for base in 'ACGT'}
    for i in range(n):
        for j in range(m):
            base = collection[j][i]
            profile[base][i] += 1
    return profile

def find_consensus_seq(profile):
    consensus = ''
    n = len(list(profile.values())[0])
    for i in range(n):
        highest_count = 0
        for base in 'ACGT':
            current_count = profile[base][i]
            if current_count > highest_count:
                highest_count = current_count
                most_frequent_base = base
        consensus += most_frequent_base
    return consensus

if __name__ == '__main__':
    if '/' in sys.argv[1]:
        ids, seqs = extract_seqs_from_fasta(sys.argv[1])
        profile = generate_profile_matrix(seqs)
        result = find_consensus_seq(profile)
    print(result)
    for base, counts in profile.items():
        print(base + ':', *counts)
