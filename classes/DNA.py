class DNA:
    DNA_ALPHABET = 'ACGTN'
    REPLICATION_MAP = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    DNA_STOP_CODONS = ['TAA', 'TAG', 'TGA']
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

    def __init__(self, seq, identifier=None):
        self.seq = seq.upper()
        self._validate_bases()
        self.RNA = self.transcribe()
        if identifier: self.identifier = identifier

    def _validate_bases(self):
        for base in self.seq:
            if base not in self.DNA_ALPHABET:
                raise Exception(f"Input string must be composed of elements in {self.DNA_ALPHABET}")

    def complement(self, seq=None):
        """ Returns the complement of a DNA string. """
        if seq:
            return ''.join([self.REPLICATION_MAP[base] for base in seq])
        return ''.join([self.REPLICATION_MAP[base] for base in self.seq])

    def reverse(self, seq = None):
        """ Returns the reverse of a DNA string. """
        if seq:
            return seq[::-1]
        return self.seq[::-1]

    def reverse_complement(self):
        return self.complement(self.reverse(self.seq))

    def transcribe(self):
        return self.seq.replace('T', 'U')

    def has_start_codon(self):
        """
        Checks for the presence of a DNA start codon within the sequence.
        If a start codon is present, this returns the starting index of the codon.
        A return value of -1 indcates the absence of the start codon.
        """
        start_idx = self.seq.find('ATG')
        return start_idx

    def has_stop_codon(self):
        """
        Checks for the presence of DNA stop codons within the sequence.
        If at least one stop codon is present, this returns the starting index of the codon.
        A return value of -1 indicates the absence of stop codons.
        """
        for stop_codon in self.DNA_STOP_CODONS:
            stop_idx = self.seq.find(stop_codon)
            if stop_idx != -1:
                return stop_idx
        return -1

    def get_reading_frames(self):
        return [self.seq[i:len(self.seq) - (i*2 % 3)] for i in range(3)]

    def get_open_reading_frames(self):
        """
        An open reading frame (ORF) is defined as a reading frame that contains BOTH start and stop codons.
        Returns a list of ORFs derived from a sequence's reading frames.
        """
        orfs = []
        reading_frames = self.get_reading_frames()
        for potential_orf in reading_frames:
            if potential_orf.has_start_codon() and potential_orf.has_end_codon():
                orfs.append(potential_orf)
        return orfs

    def translate(self, offset=0, check_stop_codon=True, include_stop_codon=True):
        """
        Returns the amino acid sequence of a DNA string. By default, it checks for the presence of both
        start and stop codons. Translation initiates and terminates at the first occurrence of a start and
        stop codons, respectively.
        """
        raw_peptide = ''
        # adjust sequence based on offset parameter
        seq = self.seq[offset:]
        # trim sequence so that len(seq) % 3 == 0
        n = len(seq)
        if n % 3 != 0:
            seq = seq[:-(n % 3)]
        # translate reading frame into raw peptide
        for i in range(0, len(seq), 3):
            codon = self.DNA_CODON_MAP[seq[i:i+3]]
            if codon == '_':
                if include_stop_codon:
                    raw_peptide += codon
            else:
                raw_peptide += codon

        # validate that the raw peptide has both start ('M') and stop ('_') codons
        if 'M' in raw_peptide and '_' in raw_peptide:
            start = raw_peptide.find('M')
            end = raw_peptide.find('_', start + 1)
            processed_peptide = raw_peptide[start:end+1]
            start_idx = (start * 3) + 2
            return start_idx, processed_peptide
        else:
            print('No valid ORF due to the absence of either/both start and stop codons')
            return None

    def count_repeats(self, n):
        counts = {}
        for i in range(len(self.seq)-n+1):
            sub = self.seq[i:i+n]
            if sub in counts:
                counts[sub] += 1
            else:
                counts[sub] = 1
        return counts
