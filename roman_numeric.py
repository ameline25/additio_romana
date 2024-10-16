ROMAN_DIGITS = {"M": 1000,
                "CM": 900, "D": 500, "CD": 400,
                "C": 100,
                "XC": 90, 'L': 50, "XL": 40,
                "X" : 10,
                "IX": 9, "V" : 5, "IV": 4,
                "I": 1}

def verification_syntaxique(saisie: str)-> bool:
     """ Retourne True si le nombre est correct"""
    for digit in saisie:
        # chiffres romains ?
        if digit not in ROMAN_DIGITS:
            print(f"ERRARE {saisie}: caractère romain {digit} invalide.")
            return False
        # quantité des chiffres romains ?
        if digit in ["M", "C", "X", "I"] and  digit * 4 in saisie:
            print(f"ERRARE {saisie}: nombre de {digit} invalide.")
            return False

    # ordre des chiffres romains
    test_saisie = saisie
    work_list =  list(ROMAN_DIGITS.keys())
    temp_list = []  # liste temporaire stockant les chiffres testés
    for key in work_list:
        if test_saisie[0:len(key)] == key:
            test_saisie = test_saisie.strip(key)
            if key in temp_list and test_saisie != "":  # utilisation d'une clé déja vérifiée
                print(f"ERRARE {saisie}: {key} déja utilisé.")
                return False
        else:
            if key in ["CM", "D", "CD"]:
                temp_list = temp_list + ["CM", "D", "CD"]
            elif key in ["XC", "L", "XL"]:
                temp_list = temp_list + ["XC", "L", "XL"]
            elif key in ["IX", "VI", "VI"]:
                temp_list = temp_list + ["IX", "VI", "IV"]
            else
                temp_list.append(key) # mémorise les clés déja vérifiées
    if test_saisie != "": # toutes les clés ont été vérifiées et il reste des chiffres romains
        print(f"ERRARE {saisie}: enchainement {saisie.replace(test_saisie,"")}-{test_saisie} invalide")
        return False
    return True


def arabic_convert(saisie: str) -> int:
    """ Retourne le nombre arabe correspondant à la saisie romaine
                 ou 0 et le motif en cas de nombre invalide"""
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
                pass
    # retourner nombre
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
    decimal_list = roman_list = []
    guess_ =  additio_romana.replace(" ", "")   # purge les "espaces"
    if '+' not in guess:
        print("La saisie n'est pas une addition!")
        exit()
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
        print(f"{" " * 13 + "_" * 2}\nNUMERI SUPRA IV NON ACCEPTI")
        exit()

    # convertir et retourner le résultat
    return roman_convert(result)

if __name__ == "__main__":

    # tests
    print(f"conversion en chiffres arabes : {arabic_convert("MMDCMLIV")}")

    print(f"conversion en chiffres romains: {roman_convert(2954)} ")

    print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")
    guess = input("saisie utilisateur : ")
    print(add_romans(guess))
