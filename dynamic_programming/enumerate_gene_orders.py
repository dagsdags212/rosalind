"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""
import sys
from itertools import permutations

def count_permutations(n):
    """ Returns a count of all possible permutations for a set consisting of [1, n]. """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * count_permutations(n-1)

def display_permutations(n):
    permIter = permutations(range(1, n+1))
    perms = []
    for p in permIter:
        p = list(map(str, p))
        p = ' '.join(p)
        perms.append(p)
    return perms

if __name__ == '__main__':
    n = int(sys.argv[1])
    result = count_permutations(n)
    perms = display_permutations(n)
    with open('./output.txt', 'w') as fh:
        fh.writelines(str(result) + '\n')
        for line in perms:
            fh.writelines(line + '\n')
    fh.close()
