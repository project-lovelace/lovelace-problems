def babylonian_sqrt(S):
    if S == 0:
        return 0

    if S < 0:
        return "invalid"

    x_n = 10
    while abs(x_n ** 2 - S) / S > 1e-10:
        x_n = 0.5 * (x_n + S / x_n)

    return x_n

