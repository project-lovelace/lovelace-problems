v = 3.0  # [km/s]

def solution(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    r1, r2, r3 = v*t1, v*t2, v*t3

    # TODO: Find my derivation and write down the steps/logic here.
    # Setting up the equations, we get two simultaneous linear equations for
    # x0 and y0, namely ax + by = e and cx + dy = f where

    a = 2*(x2-x1)
    b = 2*(y2-y1)
    c = 2*(x3-x1)
    d = 2*(y3-y1)
    e = r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2
    f = r1**2 - x1**2 - y1**2 - r3**2 + x3**2 + y3**2

    # Solving ax + by = e and cx + dy = f for x,y gives
    x = (b*f - d*e) / (b*c - a*d)
    y = (c*e - a*f) / (b*c - a*d)

    return x, y
