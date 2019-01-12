def wind_chill(T, v):
    return 13.12 + 0.6215 - 11.37*v**0.16 + 0.3965*T*v**0.16
