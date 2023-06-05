# Make sure to add module to PYTHONPATH by running the following command in cmd:
# set PYTHONPATH=%PYTHONPATH%;C:\Users\Janjan\Desktop\Rosalind\helpers

import sys

def extract_seqs_from_fasta(fasta):
    """ Returns a list of identifiers and reads from a FASTA file. """
    ids, seqs = [], []
    with open(fasta, 'r') as fh:
        lines = fh.readlines()
        current_seq = ''
        for line in lines:
            line = line.strip()
            if line[0] != '>':
                current_seq += line
            else:
                if current_seq:
                    seqs.append(current_seq)
                ids.append(line[1:])
                current_seq = ''
        seqs.append(current_seq)

    assert len(ids) == len(seqs), "Must return an equal count of ids and sequences"
    return ids, seqs
