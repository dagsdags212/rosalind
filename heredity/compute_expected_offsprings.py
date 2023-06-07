"""
For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average
 of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not
possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example,
this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b,
then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a
given factor. In order, the six given integers represent the number of couples having the following genotypes:

    GENOTYPES = {
        1: ['AA', 'AA'],
        2: ['AA', 'Aa'],
        3: ['AA', 'aa'],
        4: ['Aa', 'Aa'],
        5: ['Aa', 'aa'],
        6: ['aa', 'aa'],
    }

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""
import sys
from law_of_segregation import get_progeny_count

GENOTYPE_PAIRS = [
    ['AA', 'AA'],
    ['AA', 'Aa'],
    ['AA', 'aa'],
    ['Aa', 'Aa'],
    ['Aa', 'aa'],
    ['aa', 'aa'],
]

def calculate_expected_offsprings(parents_list):
    denom = sum(parents_list) * 2
    expected_offsprings = 0

    for count, parents in zip(parents_list, GENOTYPE_PAIRS):
        if count > 0:
            g1, g2 = parents
            progenies = get_progeny_count(g1, g2)
            # calculate the probability of getting a either an AA or Aa offspring
            if 'AA' in progenies and 'Aa' in progenies:
                expected_offsprings += ((progenies['AA'] + progenies['Aa']) / 4) * 2 * count
            elif 'AA' in progenies:
                expected_offsprings += (progenies['AA'] / 4) * 2 * count
            elif 'Aa' in progenies:
                expected_offsprings += (progenies['Aa'] / 4) * 2 * count

    return expected_offsprings

if __name__ == '__main__':
    path = sys.argv[1]
    reads = ''
    with open(path, 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            reads += line.strip()
    fh.close()
    parents_list = list(map(int, reads.split(' ')))
    result = calculate_expected_offsprings(parents_list)
    print(result)
