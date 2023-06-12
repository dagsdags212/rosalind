"""
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the
same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is
derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
"""
import sys

def reverse_complement(seq):
    DNA_COMPLEMENT_MAP = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    rc = ''
    for base in seq:
        rc = DNA_COMPLEMENT_MAP[base] + rc
    return rc

def trim_seq(seq, start=0):
    n = len(seq[start:])
    if n % 3 != 0:
        return seq[start:-(n%3)]
    return seq

def translate(seq, strict_start=True, start=0):
    from translate import RNA_CODON_MAP
    """ Returns a peptide sequence derived from a given DNA strand.
        ARGUMENTS:
            seq - string; the DNA sequence to be transcribed and translated
            strict_start - boolean; if True, translation is only initiated if a start codon is present, defaults to True.
            start - integer; indicates the offset to start translation, defaults to 0
    """
    # ensures that the DNA sequence starts at the indicated offset and has a length divisible by 3
    seq = seq[start:]
    if len(seq) % 3 != 0:
        seq = trim_seq(seq)
    # transcibe DNA to RNA
    rna_strand = seq.replace('T', 'U')

    peptides = []
    current_peptide = ''
    for i in range(0, len(rna_strand), 3):
        codon = rna_strand[i:i+3]
        if codon == 'AUG':
            current_peptide += 'M'
            for j in range(i+3, len(rna_strand), 3):
                c = rna_strand[j:j+3]
                if RNA_CODON_MAP[c] == '_':
                    peptides.append(current_peptide)
                    current_peptide = ''
                    i += j
                    break
                current_peptide += RNA_CODON_MAP[c]

    return peptides

def translate_orfs(seq):
    orfs = []
    for i in range(3):
        pep = translate(seq, start=i)
        pep_rc = translate(reverse_complement(seq), start=i)
        orfs.extend(pep)
        orfs.extend(pep_rc)
        # print(pep, pep_rc)
    return list(set(orfs))

if __name__ == '__main__':
    sys.path.append('C:\\Users\\Janjan\\Desktop\\rosalind\\helpers')
    from parse_fasta import extract_seqs_from_fasta
    path = sys.argv[1]
    ids, seqs = extract_seqs_from_fasta(path)
    unique_sequences = set()
    for seq in seqs:
        orfs = translate_orfs(seq)
        for orf in orfs:
            unique_sequences.add(orf)
    print(*unique_sequences, sep='\n')

