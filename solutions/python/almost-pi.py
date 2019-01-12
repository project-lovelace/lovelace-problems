def almost_pi(N):
    return 4 * sum([(-1)**k / (2*k+1) for k in range(N)])
