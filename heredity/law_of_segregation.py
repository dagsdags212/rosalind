"""
Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different
distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable
corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball).
The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents
all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from
the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
import sys

def get_progeny_count(g1, g2):
    """ Returns a dictionary containing the counts of each possible progeny produced by breeding g1 and g2. """
    progenies = {}
    for n in g1:
        for m in g2:
            # ensures that the dominant allele goes first
            genotype = n + m if n < m else m + n
            if genotype in progenies:
                progenies[genotype] += 1
            else:
                progenies[genotype] = 1
    return progenies

def compute_probability(k, m, n):
    """
    Returns the probability of two randomly selected mating organisms would produce a progeny possessing at least one dominant allele.
    The following genotype convention was used:
        HH - homozygous dominant
        Hh - heterozygous
        hh - homozygous recessive
    """
    total_counts = {genotype: 0 for genotype in ['HH', 'Hh', 'hh']}
    # generate the genotypes of all parents based on their counts
    genotypes = ['HH' for a in range(k)] + ['Hh' for b in range(m)] + ['hh' for c in range(n)]
    # generate the progeny counts resulting from all possible breeding pairs (assumes no self-breeding)
    progeny_counts = []
    for i, p1 in enumerate(genotypes):
        for j, p2 in enumerate(genotypes):
            if i != j:
                progeny_counts.append(get_progeny_count(p1, p2))
    # consolidate all genotype counts in total_counts map
    for pcount in progeny_counts:
        for genotype, count in pcount.items():
            total_counts[genotype] += count
    # get the total progeny count
    denom = sum(list(total_counts.values()))
    # compute for the probability of getting a homozygous recessive offspring
    p_hh = total_counts['hh'] / denom
    # compute for the probability of getting either a homozygous dominant or heterozygous offspring
    return 1 - p_hh

if __name__ == '__main__':
    k, m, n = list(map(int, sys.argv[1:]))
    result = compute_probability(k, m, n)
    print(result)
