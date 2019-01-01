import julia

j = julia.Julia()
j.include("habitable-exoplanet.jl")

user_input = (1.45, 2.28)

user_output = j.habitable_exoplanet(*user_input)

print(user_input)
print(user_output)
