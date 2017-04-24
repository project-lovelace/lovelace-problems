# problem2.py
# Polymerase chain reaction

# Featuring the EcoRII restriction enzyme:
#
# Before:         After:
#                      insertion
#                        vvvvv
# 5' NNCCWGGNN    5'---NN     CCWGGNN---3'
# 3' NNGGWCCNN    3'---NNGGWCC     NN---5'

import random

from problems.abstract_problem import AbstractProblem


class Problem3(AbstractProblem):
    def generate(self):
        dna_length = random.randint(5, 10)
        extra_sites = random.randint(1, 2)
        strand_length = random.randint(3, 10)

        sequence = self.generate_dna_sequence(dna_length)
        sequence = self.randomly_insert_extra_sites(sequence, extra_sites)
        strand = self.generate_dna_sequence(strand_length)

        problem = {'sequence': sequence, 'strand': strand}
        return problem, None

    @staticmethod
    def generate_dna_sequence(length):
        return ''.join(random.choice('ATGC') for _ in range(length))

    @staticmethod
    def randomly_insert_extra_sites(sequence, n):
        # Insert the string "CCWGG" (W = A or T) at n random locations of the
        # string sequence.
        # TODO: Does this run in O(n)?
        length = len(sequence)
        for _ in range(length):
            site = 'CC' + random.choice('AT') + 'GG'
            pos = random.randint(0, length-1)
            sequence = sequence[:pos] + site + sequence[pos:]
        return sequence

    @staticmethod
    def dna_complement(seq):
        base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        complement = [base_pairs[base] for base in list(seq)]
        return ''.join(complement)

    def solve(self, problem):
        sequence = problem['sequence']
        strand = problem['strand']

        # TODO: Will not work if strand contains 'CCTGG'.
        sequence = sequence.replace('CCAGG', strand + 'CCAGG')
        sequence = sequence.replace('CCTGG', strand + 'CCTGG')
        complement = self.dna_complement(sequence)

        solution = {'complement': complement}
        return solution

    def verify(self, proposed, actual):
        return proposed == actual

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

if __name__ == '__main__':
    Problem3().test()
