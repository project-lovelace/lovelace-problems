from fractions import Fraction
from scipy.special import binom

def bernoulli(n):
    B = (n+2) * [Fraction(0, 1)]
    B[0] = Fraction(1, 1)
    B[1] = Fraction(-1, 2)

    for i in range(2, n+1):
        B[i] = -sum([Fraction(int(factorial(i)/(factorial(k)*factorial(i - k))), (i+1-k)) * B[k]  for k in range(0, i)])

    return B[n].numerator, B[n].denominator
