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

        # Determination des séquences interdites
        roman_symbols = ["I", "V", "X", "L", "C", "M"]
        forbidden_sequences = [f"{s1}{s2}{s1}" for s1 in roman_symbols for s2 in roman_symbols if s1 != s2]
        for exception in ["MCM", "CXC", "XIX"]:
            forbidden_sequences.remove(exception)

        error_message = (
            next((f"sequence '{seq}' interdite" for seq in forbidden_sequences if seq in self.label), None),
            next((f"{digit} n'est pas un chiffre romain" for digit in self.label if digit not in roman_symbols), None),
            next((f"répétition {digit} erronée." for digit in self.label if digit in ["M", "C", "X", "I"] and digit * 4\
                  in self.label), None),
            next((f"répétition {key} erronée." for key in ["CM", "D", "CD", "XC", "L", "XL", "IX", "V", "IV"] if
                  self.label.count(key) > 1), None)
                        )

        for key in work_list:
            while test_saisie[0:len(key)] == key:  # tant qu'il en reste
                test_saisie = test_saisie[len(key):]  # on supprime
        if test_saisie != "":  # une fois le dictionnaire épuisé, test_saisie devrait être vide !
            message = f"enchainement {self.label.replace(test_saisie,"")} - {test_saisie} erroné"
            return False, error_message

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

    add_result = 0  # initialisation de la somme
    # parcourir les caractères de saisie et mettre à jour add_result ou afficher un message explicatif
    for number in "".join(saisie.split()).split("+"):
        if Roman(number).validity:
            add_result = Roman(number).value
        else:
            return f"COMPUTATIO IMPOSSIBILILIS : {number} ({Roman(number).anomaly})"

    return f"             __\nNUMERI SUPRA IV NON ACCEPTI" if add_result > 3999 else roman_convert(add_result)


if __name__ == "__main__":

    # tests
    while True:
        # print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")

        guess = input("saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()
        print(add_romans(guess))
