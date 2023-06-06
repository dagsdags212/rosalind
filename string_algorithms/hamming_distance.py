"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""
import sys

def hamming_distance(s, t):
    assert len(s) == len(t), "s and t must be of equal length"
    dist = 0
    # compare bases of s and t at current index and increment dist by 1 for every mismatch
    for idx in range(len(s)):
        if s[idx] != t[idx]:
            dist += 1
    return dist

if __name__ == '__main__':
    if len(sys.argv) > 2:
        result = hamming_distance(sys.argv[1], sys.argv[2])
    else:
        path = sys.argv[1]
        with open(path, 'r') as fh:
            s = fh.readline().strip()
            t = fh.readline().strip()
        fh.close()
        result = hamming_distance(s, t)

    print(result)
