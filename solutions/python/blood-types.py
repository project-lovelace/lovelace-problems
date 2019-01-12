def survive(patient_blood_type, donated_blood):
    if len(donated_blood) == 0:
        return False

    b = patient_blood_type

    if b == "AB+" or "O-" in donated_blood:
        return True

    if b == "A+":
        if "A+" in donated_blood or "A-" in donated_blood or "O+" in donated_blood:
            return True

    if b == "O+":
        if "O+" in donated_blood:
            return True

    if b == "B+":
        if "B+" in donated_blood or "B-" in donated_blood or "O+" in donated_blood:
            return True

    if b == "A-":
        if "A-" in donated_blood:
            return True

    if b == "O-":
        if "O-" in donated_blood:
            return True

    if b == "B-":
        if "B-" in donated_blood:
            return True

    if b == "AB-":
        if "AB-" in donated_blood or "A-" in donated_blood or "B-" in donated_blood:
            return True

    return False
