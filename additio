ROMAN_DIGITS = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                "XC": 90, 'L': 50, "XL": 40, "X" : 10,
                "IX": 9, "V" : 5, "IV": 4, "I": 1}

def identification(saisie):
    """ Retourne le nombre correspond à la saisie romaine"""
    nombre = 0
    work_list = list(ROMAN_DIGITS.keys())
    #pour clé dans work_list
        # tant que clé présent dans saisie
            # ajouter valeur de clé  à nombre
            # effacer clé de saisie
        # effacer clé de work_liste
    # retourner nombre
    pass

def transcription(nombre) :
    """ Retourne le nombre converti en nombre romain"""
    # inverser le dictionnaire?
    work_list = list(ROMAN_DIGITS.values())
    roman = ""
    # pour valeur dans work_list
        # tant que nombre > valeur
            # ajouter clé correspondant à valeur à roman = clé du dictionnaire inversé
            # soustraire valeur de nombre
        # effacer valeur de work_list
    # retourner roman
    pass


def verification_syntaxique(saisie):
    syntax_error = ["IM", "XM", "IC"]
    """ Retourne True si le nombre est correct"""
    for digit in saisie:
        # chiffres romains ?
        if digit not in ROMAN_DIGITS:
            print(f"{saisie}, caractère romain {digit} invalide")
            return False
        # quantité des chiffres romains ?
        if digit in ["M", "C", "X", "I"] and saisie.count(digit) > 3:
            print(f"{saisie}, nombre de {digit} invalide")
            return False
        elif digit in ["D", "L", "V"] and saisie.count(digit)  > 1:
            return False

    # ordre des chiffres romains
    test_saisie = saisie
    work_list =  list(ROMAN_DIGITS.keys())
    temp_list = []  # liste temporaire stockant les chiffres testés
    for key in work_list:
        while test_saisie[0:len(key)] == key:
            test_saisie = test_saisie[len(key):]
            if key in temp_list and test_saisie != "":
                print(f"{saisie}, ordre des chiffres invalide")
                return False
        temp_list.append(key)
    return True


def add_romans(additio_romana):
    decimal_list = roman_list = []
    guess =  additio_romana.replace(" ", "")   # purge les "espaces"
    roman_list = guess.split("+")  # liste les nombres à additionner
    print(roman_list)
    # affiche les nombres rejetés et leur motif
    for number in roman_list:
        if verification_syntaxique(number):
            decimal_list.append(identification(number))

        else:
            return "Operation invalide"

    # additionner les éléments de la liste decimal_list
    # convertir le résultat
    # retourner le résultat

print(f"ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")
guess = input("saisie utilisateur : ")
print(add_romans(guess))
