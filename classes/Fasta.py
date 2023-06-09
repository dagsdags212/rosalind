class FastaIdentifier:
    """
    Each identifier starts with the '>' character and is associated with a sequence.
    The pipe symbol ('|') is commonly used to separate details that map to each sequence.
    The format, as arranged from left to right, is as follows:
        1. Genbank identifier
        2. GI identifier
        3. Database source
        4. Accession number
        5. Additional sequence information (free form)
    """
    DATABASE_SOURCE = {
        'lcl': 'local',
        'bbs': 'GenInfo backbone seqid',
        'bbm': 'GenInfo backbone moltype',
        'gim': 'GenInfo',
        'gb' : 'GenBank',
        'emb': 'EMBL',
        'pir': 'PIR',
        'sp' : 'SWISS-PRO',
        'pat': 'patent',
        'pgp': 'pre-grant patent',
        'ref': 'RefSeq',
        'gnl': 'general database reference',
        'gi' : 'GenInfo integrated database',
        'dbj': 'DDBJ',
        'prf': 'PRF',
        'pdb': 'PDB',
        'tpg': 'third-party GenBank',
        'tpe': 'third-party EMBL',
        'tpd': 'third-party DDBJ',
        'tr' : 'TrEMBL'
    }

    def __init__(self, identifier):
        self.identifier = identifier
        self._parseIdentifier()

    def __str__(self):
        return f"""
        Source: {self.db_source}
        Accession number: {self.accession_num}
        Details: {self.details}
        """

    def _parseIdentifier(self, sep='|'):
        _, _, db_source, accession_num, details = self.identifier.split(sep)
        self.db_source = self.DATABASE_SOURCE[db_source]
        self.accession_num = accession_num
        self.details = details

class FastaFile:
    def __init__(self, filename):
        fileFormat = filename.split('.')[-1]
        assert fileFormat in ['fa', 'fasta'], 'File format must be .fa or .fasta'
        self.filename = filename
        self.reads = self._parseFile()
        self.seqs = self._parseSeqs()
        self.identifiers = self._parseIdentifiers()

    def _parseFile(self):
        """
        Returns a dictionary mapping read identifiers to its corresponding DNA
        sequence. Gets called upon instantiating the class.
        """
        reads = {}
        try:
            fh = open(self.filename, 'r')
            for line in fh:
                line = line.rstrip()
                if line[0] == '>':
                    current_read = line
                    if current_read not in reads:
                        reads[current_read] = ''
                else:
                    reads[current_read] += line
            fh.close()
            return reads
        except IOError:
            print('Invalid file path!')

    def _parseSeqs(self):
        """ Iteraters over read values and returns a list of sequences. """
        assert self.reads != None
        return [seq for seq in self.reads.values()]

    def _parseIdentifiers(self):
        """ Iterates over read keys and returns a list of fastaIdentifier objects. """
        assert self.reads != None
        return [FastaIdentifier(identifier) for identifier in self.reads.keys()]

    def get_longest_sequence(self):
        """ Returns the identifier and sequence of the longest read in terms of length. """
        identifier, seq = sorted(self.reads.items(), key=lambda x: len(x[1]))[-1]
        return identifier, seq

    def get_shortest_sequence(self):
        """ Returns the identifier and sequence of the shortest read in terms of length. """
        identifier, seq = sorted(self.reads.items(), key=lambda x: len(x[1]))[0]
        return identifier, seq

