function habitable_exoplanet(L, r)
    rᵢ = √(L / 1.11)  # [AU]
    rₒ = √(L / 0.53)  # [AU]

    if r < rᵢ
        return "too hot"
    elseif r > rₒ
        return "too cold"
    else
        return "just right"
    end
end
