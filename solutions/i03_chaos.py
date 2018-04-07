def solution(r):
    x = [0.5]
    for _ in range(50):
        x.append(r * x[-1] * (1 - x[-1]))
    return x
