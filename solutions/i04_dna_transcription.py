def dna_complement(seq):
    base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement = [base_pairs[base] for base in list(seq)]
    return ''.join(complement)

def solution(dna):
    return dna_complement(dna)
