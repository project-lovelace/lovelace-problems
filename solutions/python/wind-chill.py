def wind_chill(T_a, v):
    return 13.12 + 0.6215*T_a - 11.37*v**0.16 + 0.3965*T_a*v**0.16
