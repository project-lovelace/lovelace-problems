def babylonian_sqrt(S):
    x_n = 10
    while abs(x_n**2 - S) / S > 1e-10:
        x_n = 0.5 * (x_n + S/x_n:
    return x_n
