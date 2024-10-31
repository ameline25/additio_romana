ROMAN_SYMBOLS = ["I", "V", "X", "L", "C", "D", "M"]
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
        self.value = self.get_roman_value()

    def is_roman(self) ->bool:
        """ Retourne True si le nombre est correct sinon False"""
        # Utilisation de chiffres non romains ou de plus 4 chiffres identiques consécutifs ou
        for digit in self.label:
            if digit not in ROMAN_SYMBOLS or (digit in ["M", "C", "X", "I"] and digit * 4 in self.label)\
                    or (digit in ["D", "L", "V"] and self.label.count(digit) > 1):
                return False

        # Détermination des séquences interdites
        forbidden_sequences = [f"{s1}{s2}{s1}" for s1 in ROMAN_SYMBOLS for s2 in ROMAN_SYMBOLS if s1 != s2]
        for exception in ["MCM", "CXC", "XIX"]:
            forbidden_sequences.remove(exception)  # réintégration des exceptions
        for seq in forbidden_sequences:
            if seq in self.label:
                return False

        # conformité de l'ordre des séquences
        test_saisie = self.label
        for key in list(ROMAN_DIGITS.keys()):  # supprime key tant qu'il est présent au début...
            while test_saisie[0:len(key)] == key:
                test_saisie = test_saisie[len(key):]
        if test_saisie != "":  # ... pour obtenir une chaine vide
            return False
        return True

    def get_roman_value(self) -> int:
        """ Retourne la valeur entière correspondante à la saisie romaine"""
        nombre, temp_saisie = 0, self.label  # initialisation

        for key, valeur in ROMAN_DIGITS.items():
            while temp_saisie[0:len(key)] == key:
                #  augmente nombre de la valeur de key tant qu'il est présent
                nombre += valeur
                temp_saisie = temp_saisie[len(key):]
        return nombre

    @staticmethod
    def roman_convert(nombre: int) -> str:
        """ Retourne la transcription romaine du nombre"""
        roman = ""  # initialisation

        for symbol, valeur in ROMAN_DIGITS.items():
            n = nombre // valeur
            roman = roman + symbol * n
            nombre -= n * valeur
        return roman

    @staticmethod
    def add_romans(saisie :str) -> str:
        if '+' not in saisie:
            return "La saisie n'est pas une addition!"

        add_result = 0  # initialisation de la somme
        # parcourir les caractères de saisie et mettre à jour add_result ou afficher un message d'erreur explicatif
        for number in "".join(saisie.split()).split("+"):
            if Roman(number).validity:
                add_result += Roman(number).value
            else:
                return f"COMPUTATIO IMPOSSIBILILIS : Syntaxe romaine '{number}' erronée"

        return f"             __\nNUMERI SUPRA IV NON ACCEPTI" if add_result > 3999\
            else Roman(saisie).roman_convert(add_result)


if __name__ == "__main__":

    # tests
    while True:
        print("\nADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")
        guess = input("Saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()
        print(Roman.add_romans(guess))
