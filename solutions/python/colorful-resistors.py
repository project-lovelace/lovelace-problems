digits = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

multiplier = {
    'pink': 0.001,
    'silver': 0.01,
    'gold': 0.1,
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 10 ** 3,
    'yellow': 10 ** 4,
    'green': 10 ** 5,
    'blue': 10 ** 6,
    'violet': 10 ** 7,
    'grey': 10 ** 8,
    'white': 10 ** 9
}

tolerance = {
    'none': 0.2,
    'silver': 0.1,
    'gold': 0.05,
    'brown': 0.01,
    'red': 0.02,
    'green': 0.005,
    'blue': 0.0025,
    'violet': 0.001,
    'grey': 0.0005
}


def resistance(colors):
    n_bands = len(colors)

    nominal_R = 0
    minimum_R = 0
    maximum_R = 0

    if n_bands == 1 and colors[0] == 'black':
        nominal_R = 0
        minimum_R = 0
        maximum_R = 0
    elif n_bands == 4:
        nominal_R = 10 * digits[colors[0]] + digits[colors[1]]
        nominal_R *= multiplier[colors[2]]
        minimum_R = (1 - tolerance[colors[3]]) * nominal_R
        maximum_R = (1 + tolerance[colors[3]]) * nominal_R
    elif n_bands == 5:
        nominal_R = 100 * digits[colors[0]] + 10 * digits[colors[1]] + digits[colors[2]]
        nominal_R *= multiplier[colors[3]]
        minimum_R = (1 - tolerance[colors[4]]) * nominal_R
        maximum_R = (1 + tolerance[colors[4]]) * nominal_R
    else:
        pass

    return nominal_R, minimum_R, maximum_R
