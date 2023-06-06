"""
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
"""
import sys
from parse_fasta import extract_seqs_from_fasta
from translate import RNA_CODON_MAP, translate

def splice(seq, introns):
    for intron in introns:
        start = seq.find(intron)
        seq = seq[:start] + seq[start + len(intron):]
    rna = seq.replace('T', 'U')
    peptide = translate(rna)
    return peptide

if __name__ == '__main__':
    path = sys.argv[1]
    _, seqs = extract_seqs_from_fasta(path)
    seq, introns = seqs[0], seqs[1:]
    result = splice(seq, introns)
    print(result)
