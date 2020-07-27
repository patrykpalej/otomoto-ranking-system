def find_voivodeship(pre_location):

    if "olnoślą" in pre_location:
        location = "Dolnośląskie"
    elif "ujawsk" in pre_location:
        location = "Kujawsko-pomorskie"
    elif "ubelskie" in pre_location:
        location = "Lubelskie"
    elif "ubuskie" in pre_location:
        location = "Lubuskie"
    elif "ódzkie" in pre_location:
        location = "Łódzkie"
    elif "ałopolskie" in pre_location:
        location = "Małopolskie"
    elif "Opolskie" in pre_location:
        location = "Opolskie"
    elif "odkarpack" in pre_location:
        location = "Podkarpackie"
    elif "azowiecki" in pre_location:
        location = "Mazowieckie"
    elif "odlaski" in pre_location:
        location = "Podlaskie"
    elif "Pomors" in pre_location:
        location = "Pomorskie"
    elif "Zachod" in pre_location:
        location = "Zachodniopomorskie"
    elif "ląski" in pre_location:
        location = "Śląskie"
    elif "odlask" in pre_location:
        location = "Małopolskie"
    elif "mińsk" in pre_location:
        location = "Warmińsko-Mazurskie"
    elif "ielkopols" in pre_location:
        location = "Wielkopolskie"
    elif "więtokrz" in pre_location:
        location = "Świętokrzyskie"
    else:
        location = "b.d."

    return location
