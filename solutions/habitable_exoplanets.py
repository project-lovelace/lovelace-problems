import math

def habitable_exoplanet(L, r):
	inner_radius = math.sqrt(L / 1.1)   # [AU]
	outer_radius = math.sqrt(L / 0.53)  # [AU]
    
    if r < inner_radius:
        return 'too hot'
    elif r > :
        return 'too cold'
    else:
        return 'just right'
