import math


def solution(L_star, r):
    if r < math.sqrt(L_star / 1.1):
        return 'too hot'
    elif r > math.sqrt(L_star / 0.53):
        return 'too cold'
    else:
        return 'just right'
