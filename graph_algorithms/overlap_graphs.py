"""
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment;
the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop
is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is
connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops
in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
"""
import sys
from parse_fasta import extract_seqs_from_fasta

class Node:
    def __init__(self, id, seq):
        self.id = id
        self.seq = seq
        self.neighbors = []

    def prefix(self, l=3):
        return self.seq[:l]

    def suffix(self, l=3):
        return self.seq[len(self.seq)-l:]

    @staticmethod
    def check_overlap(src, dest, l=3):
        return src.suffix(l) == dest.prefix(l)

    def overlaps_with(self, node, l=3):
        has_overlap = self.suffix(l) == node.prefix(l)
        if has_overlap:
            self.neighbors.append(dest)
        return has_overlap

    def __str__(self):
        if len(self.neighbors) > 0:
            for n in self.neighbors:
                print(f"{self.seq}->{n}")
        return self.seq

if __name__ == '__main__':
    path = sys.argv[1]
    ids, seqs = extract_seqs_from_fasta(path)
    nodes =  [Node(i, s) for i, s in zip(ids, seqs)]

    overlapping_nodes = []
    for src in nodes:
        for dest in nodes:
            if src != dest:
                if src.overlaps_with(dest, 3):
                    overlapping_nodes.append((src.id, dest.id))

    for overlap in overlapping_nodes:
        print(*overlap)
