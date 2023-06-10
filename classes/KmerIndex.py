from bisect import bisect_left

class KmerIndex(object):
    """
    Creates an mapping of all k-mers in the given text to the index of
    their first left-most occurrence.
    """
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t)-k+1):
            self.index.append((t[i:i+k], i))
        self.index.sort()

    def query(self, p):
        """
        Returns a list of indices where pattern appears as a
        substring of the text.
        """
        kmer = p[:self.k]
        i = bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits
