"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""
import sys
import parse_fasta as pf

def compute_gc_content(fasta):
    ids, seqs = pf.extract_seqs_from_fasta(fasta)
    gc_contents = []
    for seq in seqs:
        current_gc_content = (seq.count('G') + seq.count('C')) / len(seq) * 100
        gc_contents.append(current_gc_content)
    max_value = max(gc_contents)
    idx_max_value = gc_contents.index(max_value)
    return ids[idx_max_value], max_value

if __name__ == '__main__':
    seq, value = compute_gc_content(sys.argv[1])
    print(seq)
    print(value)
