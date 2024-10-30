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
            forbidden_sequences.remove(exception)
        for seq in forbidden_sequences:
            if seq in self.label:
                return False
        # Exactitude de l'ordre des séquences
        test_saisie = self.label
        for key in list(ROMAN_DIGITS.keys()):
            while test_saisie[0:len(key)] == key:  # tant qu'il en reste
                test_saisie = test_saisie[len(key):]  # on supprime
        if test_saisie != "":  # on doit finalement obtenir une chaine vide
            return False
        return True

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

    @staticmethod
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

    @staticmethod
    def add_romans(saisie :str) -> str:
        if '+' not in saisie:
            return "La saisie n'est pas une addition!"

        add_result = 0  # initialisation de la somme
        # parcourir les caractères de saisie et mettre à jour add_result ou afficher un message explicatif
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
