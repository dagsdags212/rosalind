"""
For positive integers a and n, a modulo n (written a mod n in shorthand) is the remainder when a is divided by n. For example, 29 mod 11=7 because 29 = 11 x 2 + 7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a
and b are congruent modulo n if a mod n = b mod n; in this case, we use the notation a ≡ b mod n.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a x c ≡ b x d mod n.
To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""
import sys

DNA_CODON_MAP = {
'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
'TAA': '_', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
'TAG': '_', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
'TGA': '_', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G',
}

def get_reverse_translation_map():
    """ Returns a dictionary mapping each amino acid with its corresponding number of codons. """
    AMINO_ACIDS = 'ARNDCQEGHILKMFPSTWYV_'
    REVERSE_TRANSLATION_MAP = {aa: 0 for aa in AMINO_ACIDS}
    for codon in DNA_CODON_MAP.values():
        REVERSE_TRANSLATION_MAP[codon] += 1
    return REVERSE_TRANSLATION_MAP

def infer_mrna_from_peptide(peptide):
    """ Returns the number of possible mRNA sequences dervied from a given peptide.
        Calculated value is divided by module 1000000 to save memory. """
    num_rna = 1
    RT_MAP = get_reverse_translation_map()
    for aa in peptide:
        # print(f'Current amino acid is {aa} which can be encoded by {RT_MAP[aa]} codons.')
        num_rna *= RT_MAP[aa]
    # account for the 3 possible stop codons
    # print('Accounting for the three stop codons...')
    return (num_rna * 3) % 1_000_000

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path, 'r') as fh:
        peptide = fh.readline().rstrip()
    result = infer_mrna_from_peptide(peptide)
    print(result)
