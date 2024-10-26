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
        """ Retourne True et "" si le nombre est correct
                                sinon False et un message concernant l'anomalie rencontrée"""
        test_saisie = self.label

        # Determination des séquences interdites
        roman_symbols = ["I", "V", "X", "L", "C", "M"]
        forbidden_sequences = [f"{s1}{s2}{s1}" for s1 in roman_symbols for s2 in roman_symbols if s1 != s2]
        for exception in ["MCM", "CXC", "XIX"]:
            forbidden_sequences.remove(exception)

        error_message = (
            next(  # affiche un message d'erreur si une séquence interdite est trouvée
                (f"séquence '{seq}' interdite" for seq in forbidden_sequences if seq in self.label), None),
            next(  # affiche un message d'erreur si un chiffre non romain est trouvé
                (f"{digit} n'est pas un chiffre romain" for digit in self.label if digit not in roman_symbols), None),
            next(  # affiche un message d'erreur si une séquence de 4 chiffre identique est trouvée
                (f"répétition {digit} erronée" for digit in self.label if digit in ["M", "C", "X", "I"] and digit * 4\
                  in self.label), None),
            next(  # affiche un message d'erreur en cas d'une multiple présence d'une séquence unique
                (f"répétition {key} erronée" for key in ["CM", "D", "CD", "XC", "L", "XL", "IX", "V", "IV"] if
                  self.label.count(key) > 1), None)
                        )
        error_message = set(error_message)   # l'ensemble permet d'éditer le tuple retire les "None" en doublons
        error_message.remove(None)  # supprime None pour ne garder que les anomalies

        # les chiffres romains du début sont éliminés un à un dans l'ordre défini par le dictionnaire
        for key in list(ROMAN_DIGITS.keys()):
            while test_saisie[0:len(key)] == key:  # tant qu'il en reste
                test_saisie = test_saisie[len(key):]  # on supprime
        if test_saisie != "" and not error_message:
            error_message.add(f"enchainement {self.label.replace(test_saisie,"")} - {test_saisie} erroné")

        if error_message:  # en cas d'anomalie détectée
            return False, f"{self.label}: {", ".join(error_message)}" 

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
                return f"COMPUTATIO IMPOSSIBILILIS : {number} ({Roman(number).anomaly})"

        return f"             __\nNUMERI SUPRA IV NON ACCEPTI" if add_result > 3999 else Roman(saisie).roman_convert(add_result)


if __name__ == "__main__":

    # tests
    while True:
        #print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")

        guess = input("saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()

        #print(Roman.add_romans(guess))
        print(f"nom: {Roman(guess).label}")
        print(f"validité: {Roman(guess).validity}")
        print(f"anomalie: {Roman(guess).anomaly}")
        print(f"valeur: {Roman(guess).value}")
