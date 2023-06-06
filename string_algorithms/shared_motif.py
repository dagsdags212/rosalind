"""
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
import sys
import parse_fasta as pf

def find_shortest_string(collection):
    min_len = float('inf')
    for seq in collection:
        seq_len = len(seq)
        if seq_len < min_len:
            min_len = seq_len
            shortest_seq = seq
    return shortest_seq

def get_substrings(seq):
    k = len(seq) - 1
    substrings = []
    # iterate over the longest subsring to the shortest ones (min. of 2 nucleotides)
    for i in range(k, 1, -1): # 4, 3, 2
        for j in range(len(seq)-i+1): # 2, 3, 4
            substrings.append(seq[j:j+i])
    return substrings

def find_common_substring(collection):
    # find the shortest string in collection
    shortest_str = find_shortest_string(collection)
    # get all possible substrings of shortest string, arrange in decreasing length
    substrs_of_shortest_str = get_substrings(shortest_str)
    # iterate over substrings and check each string in collection for the presence of substring
    for substr in substrs_of_shortest_str:
        count = 0
        for seq in collection:
            if substr in seq:
                count += 1
        if count == len(collection):
            return substr

if __name__ == '__main__':
    from time import time
    start = time()
    ids, collection = pf.extract_seqs_from_fasta(sys.argv[1])
    result = find_common_substring(collection)
    end = time()
    print(result, end-start)

