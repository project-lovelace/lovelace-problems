def alive(blood_type, donated_blood):
    if len(donated_blood) == 0:
        return False

    if blood_type == "AB+" or "O-" in donated_blood:
        return True

    if blood_type == "A+":
        if "A+" in donated_blood or "A-" in donated_blood or "O+" in donated_blood:
            return True

    if blood_type == "O+":
        if "O+" in donated_blood:
            return True

    if blood_type == "B+":
        if "B+" in donated_blood or "B-" in donated_blood or "O+" in donated_blood:
            return True

    if blood_type == "A-":
        if "A-" in donated_blood:
            return True

    if blood_type == "O-":
        if "O-" in donated_blood:
            return True

    if blood_type == "B-":
        if "B-" in donated_blood:
            return True

    if blood_type == "AB-":
        if "AB-" in donated_blood or "A-" in donated_blood or "B-" in donated_blood:
            return True

    return False
