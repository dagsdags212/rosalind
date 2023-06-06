"""
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn-1+Fn-2 and assumed that each pair of rabbits
reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months.
See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n ≤ 100 and m ≤ 20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
import sys

def compute_mortal_rabbit_pairs(n, m):
    """ Returns the number of rabbit pairs after n months has elapsed, assuming a life expectancy of m months. """
    bunnies = [1, 1]
    months = 2
    while months < n:
        if months < m:
            bunnies.append(bunnies[-2] + bunnies[-1])
        elif months == m:
            bunnies.append(bunnies[-2] + bunnies[-1] - 1)
        else:
            bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m+1)])
        months += 1
    return bunnies[-1]

if __name__ == '__main__':
    if '/' in sys.argv[1]:
        path = sys.argv[1]
        with open(path, 'r') as fh:
            n, k = fh.readline().strip().split(' ')
        fh.close()
        n, k = int(n), int(k)
        result = compute_mortal_rabbit_pairs(n, k)
    elif len(sys.argv) == 3:
        result = compute_mortal_rabbit_pairs(int(sys.argv[1]), int(sys.argv[2]))

    print(result)
