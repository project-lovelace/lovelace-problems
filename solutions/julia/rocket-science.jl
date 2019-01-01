v_e = 2550 # rocket exhaust velocity [m/s]
M = 250000 # rocket dry mass [kg]
rocket_fuel(v) = M * (exp(v/v_e) - 1)
