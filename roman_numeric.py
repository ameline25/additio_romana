ROMAN_DIGITS = {"M": 1000,
                "CM": 900, "D": 500, "CD": 400,
                "C": 100,
                "XC": 90, 'L': 50, "XL": 40,
                "X" : 10,
                "IX": 9, "V" : 5, "IV": 4,
                "I": 1}

def verification_syntaxique(saisie: str)-> bool:
    """ Retourne True si le nombre est correct"""
    work_list = list(ROMAN_DIGITS.keys())
    test_saisie = saisie    
  
    # séquences interdites?
    forbidden_sequence = ["IVI", "IXI", "CDC", "CMC", "CXC", "XVX"]
    for sequence in forbidden_sequence:
        if sequence in saisie:
            return False
          
    # chiffres romains?
    for digit in saisie:
        if digit not in ROMAN_DIGITS:
            return False

        # suite de chiffres romains identiques?
        if digit in ["M", "C", "X", "I"] and  digit * 4 in saisie:  # chiffres répétables
            return False

    # multiple présence de chiffres devant être uniques?
    for key in work_list:
        if key in ["CM", "D", "CD", "XC", "L", "XL", "IX", "V", "IV"] and saisie.count(key) > 1:
            return False

    # ordre correct des chiffres romains?
    # les chiffres romains du début sont éliminés un à un dans l'ordre défini par le dictionnaire
    for key in work_list:
        while test_saisie[0:len(key)] == key:  # tant qu'il en reste
            test_saisie = test_saisie[len(key):]  # on supprime

    if test_saisie !="":  # une fois le dictionnaire épuisé, test_saisie devrait être vide !
        return False

    return True


def arabic_convert(saisie: str) -> int:
    """ Retourne le nombre arabe correspondant à la saisie romaine
                 ou indique saisie invalide """
    nombre = 0  # initialisation
    if verification_syntaxique(saisie):
        # Pour clé dans le dictionnaire
        for key, valeur in ROMAN_DIGITS.items():
            # si clé correspond au début de saisie
            if saisie[0:len(key)] == key:
                # tant que même clé
                while saisie[0:len(key)] == key:
                    nombre += valeur
                    # effacer clé de saisie
                    saisie = saisie[len(key):]
    else:
        nombre ="Roman syntax Error"
    return nombre


def roman_convert(nombre: int) -> str:
    """ Retourne la transcription romaine du nombre"""
    roman = ""  # initialisation
    # pour valeur dans le dictionnaire
    for symbol, valeur in ROMAN_DIGITS.items():
        n = nombre // valeur
        # concaténer roman
        roman = roman + symbol * n
        # soustraire de nombre
        nombre -= n * valeur
    # retourner roman
    return roman


def add_romans(additio_romana: str) ->str:
    decimal_list , roman_list = [], []
    guess_ =  additio_romana.replace(" ", "")   # purge les "espaces"
    if '+' not in guess_:
        return "La saisie n'est pas une addition!"
    roman_list = guess_.split("+")  # liste les nombres à additionner

    # affiche les nombres rejetés et le motif de rejet
    for number in roman_list:
        if verification_syntaxique(number):
            decimal_list.append(arabic_convert(number))
        else:
            return "COMPUTATIO IMPOSSIBILIS"

        # additionner les éléments de la liste decimal_list
    result = 0
    for number in decimal_list:
        result += int(number)
    if result > 3999:
        return f"{" " * 13 + "_" * 2}\nNUMERI SUPRA IV NON ACCEPTI"

    # convertir et retourner le résultat
    return roman_convert(result)

if __name__ == "__main__":

    # tests
    while True:
        # print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")

        guess = input("saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()
        print(add_romans(guess))
        continue
