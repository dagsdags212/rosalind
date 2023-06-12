"""
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X."
For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
>>> http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
>>> http://www.uniprot.org/uniprot/uniprot_id.
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""
import sys
import requests

def retrieve_uniprot_fasta(protein_id, format='utf-8'):
    """ Retrieves a FASTA file frop. """
    URL = f'http://www.uniprot.org/uniprot/{protein_id}.fasta'
    f = requests.get(URL)
    assert f.status_code == 200, 'Failed to retrieve data. HTTPS Status Code: %s' % (f.status_code)
    return f.content.decode(format).rstrip()

def parse_uniprot_fasta(filename):
    """ Returns a dictionary of UniProt primary/secondary IDs as keys and their
        corresponding peptide sequence as value. """
    protein_map = {}
    try:
        with open(filename, 'r') as fh:
            for line in fh:
                line = line.rstrip()
                if line[0] == '>' and line not in protein_map:
                    current_id = line
                    protein_map[line] = ''
                else:
                    protein_map[current_id] += line
        return protein_map
    except IOError:
        print('Invalid filename %s' % filename)

def parse_uniprot_string(content):
    protein_map = {}
    lines = content.split('\n')
    for line in lines:
        if line[0] == '>' and line not in protein_map:
            current_id = line
            protein_map[line] = ''
        else:
            protein_map[current_id] += line
    return protein_map

def generate_protein_index(protein_seq):
    """ Returns a dictionary mapping all protein 4-mers to their starting index.
        Index is used to find the N-glycosylation motif written as:
            N{P}[ST]{P}
    """
    index = {}
    for i in range(len(protein_seq)-3):
        substr = protein_seq[i:i+4]
        # skip further comparisons if substring does not start with N
        if not is_valid_glycosylation_motif(substr): continue
        if substr not in index:
            index[substr] =[i+1]
        else:
            index[substr].append(i+1)
    return index

def is_valid_glycosylation_motif(substr):
    return (substr[0] == 'N') and (substr[1] != 'P') and (substr[2] in 'ST') and (substr[3] != 'P')

def search_protein_motif_occurrences(protein_ids):
    proteins_with_motif = {}
    for pid in protein_ids:
        protein_id = pid
        if '_' in pid:
            protein_id = pid.split('_')[0]
        uniprot_string = retrieve_uniprot_fasta(protein_id)
        protein_map = parse_uniprot_string(uniprot_string)
        protein_seq = list(protein_map.values())[0]
        hits = generate_protein_index(protein_seq)

        if hits:
            proteins_with_motif[pid] = list(hits.values())

    for iden, idxs in proteins_with_motif.items():
        print(iden)
        print(*map(lambda x: x[0], idxs))

    return proteins_with_motif

if __name__ == '__main__':
    path = sys.argv[1]
    protein_ids = []
    with open(path, 'r') as fh:
        for line in fh:
            if line:
                protein_ids.append(line.rstrip())
    search_protein_motif_occurrences(protein_ids)
