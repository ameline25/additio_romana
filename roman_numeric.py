ROMAN_DIGITS = {"M": 1000,
                "CM": 900, "D": 500, "CD": 400,
                "C": 100,
                "XC": 90, 'L': 50, "XL": 40,
                "X": 10,
                "IX": 9, "V": 5, "IV": 4,
                "I": 1}

class Roman:
    def __init__(self, label: str):
        self.label = label
        self.validity = self.is_roman()
        self.anomaly = self.get_anomaly()
        self.value = self.get_roman_value()

    def validate_roman(self) -> (bool, str):
        """ Retourne True si le nombre est correct et un message concernant l'anomalie rencontrée"""
        work_list = list(ROMAN_DIGITS.keys())
        test_saisie = self.label

        # séquences interdites ?

        forbidden_sequence = ["IVI", "IXI", "CDC", "CMC", "CXC", "XVX"]
        for sequence in forbidden_sequence:
            if sequence in self.label:
                message = f"séquence {sequence} interdite"
                return False, message

        # chiffres romains ?
        for digit in self.label:
            if digit not in ROMAN_DIGITS:
                message = f"{digit} n'est pas un chiffre romain!"
                return False, message

            # suite de chiffres romains identiques ?
            if digit in ["M", "C", "X", "I"] and digit * 4 in self.label:  # chiffres répétables
                message = f"répétition {digit} erronée."
                return False, message

        # multiple présence de chiffres devant être uniques ?
        for key in work_list:
            if key in ["CM", "D", "CD", "XC", "L", "XL", "IX", "V", "IV"] and self.label.count(key) > 1:
                message = f"répétition {key} erronée."
                return False, message

        # ordre correct des chiffres romains ?
        # les chiffres romains du début sont éliminés un à un dans l'ordre défini par le dictionnaire
        for key in work_list:
            while test_saisie[0:len(key)] == key:  # tant qu'il en reste
                test_saisie = test_saisie[len(key):]  # on supprime

        if test_saisie != "":  # une fois le dictionnaire épuisé, test_saisie devrait être vide !
            message = f"enchainement {self.label.replace(test_saisie,"")} - {test_saisie} erroné"
            return False, message

        return True, ""

    def is_roman(self):
        valid, _ = self.validate_roman()
        return valid

    def get_anomaly(self):
        _, message = self.validate_roman()
        return message


    def get_roman_value(self) -> int:
        """ Retourne la valeur entière correspondante à la saisie romaine"""
        nombre = 0  # initialisation
        saisie = self.label
        # Pour clé dans le dictionnaire
        for key, valeur in ROMAN_DIGITS.items():
            # si clé correspond au début de saisie
            while saisie[0:len(key)] == key:
                nombre += valeur
                # effacer clé de saisie
                saisie = saisie[len(key):]
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

def add_romans(saisie: str) -> str:
    if '+' not in saisie:
        return "La saisie n'est pas une addition!"
    roman_list = "".join(saisie.split()).split("+")  # liste les nombres à additionner

    # affiche les nombres rejetés et le motif de rejet
    error = False
    decimal_list = []
    for number in roman_list:
        if Roman(number).validity:
            decimal_list.append(Roman(number).value)
        else:
            print(f"{number} : {Roman(number).anomaly}")
            error = True

    if error:
        return "COMPUTATIO IMPOSSIBILILIS"

    # additionner les éléments de la liste decimal_list
    result = sum(decimal_list)
    return f"             __\nNUMERI SUPRA IV NON ACCEPTI" if result > 3999 else roman_convert(result)


if __name__ == "__main__":

    # tests
    while True:
        # print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")

        guess = input("saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()
        print(add_romans(guess))
