def dna_complement(seq):
    base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement = [base_pairs[base] for base in list(seq)]
    return ''.join(complement)

dna_str = str(input())
print(dna_complement(dna_str))
