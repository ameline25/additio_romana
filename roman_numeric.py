ROMAN_SYMBOLS = ["I", "V", "X", "L", "C", "M"]
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

        # Détermination des séquences interdites
        forbidden_sequences = [f"{s1}{s2}{s1}" for s1 in ROMAN_SYMBOLS for s2 in ROMAN_SYMBOLS if s1 != s2]
        for exception in ["MCM", "CXC", "XIX"]:  # réintègre des séquences autorisées
            forbidden_sequences.remove(exception)

        # stockage des anomalies dans un tuple
        error_message = (
            next(  # affiche un message d'erreur si une séquence interdite est trouvée
                (f"séquence '{seq}' interdite" for seq in forbidden_sequences if seq in self.label), None),
            next(  # affiche un message d'erreur si un chiffre non romain est trouvé
                (f"{digit} n'est pas un chiffre romain" for digit in self.label if digit not in ROMAN_SYMBOLS), None),
            next(  # affiche un message d'erreur si une séquence de 4 chiffre identique est trouvée
                (f"répétition {digit} erronée" for digit in self.label if digit in ["M", "C", "X", "I"] and digit * 4\
                  in self.label), None),
            next(  # affiche un message d'erreur en cas d'une multiple présence d'une séquence unique
                (f"répétition {key} erronée" for key in ["CM", "D", "CD", "XC", "L", "XL", "IX", "V", "IV"] if
                  self.label.count(key) > 1), None)
                        )
        error_message = set(error_message)  # transformation en ensemble pour enlever les doublons
        error_message.remove(None)  # suppression du dernier None

        # test de l'ordre correct des 'digits romains' qui doit respecter celui du dictionnaire
        for key in list(ROMAN_DIGITS.keys()):
            while test_saisie[0:len(key)] == key:  # tant que test_saisie commence par key
                test_saisie = test_saisie[len(key):]  # on supprime le premier key
        if test_saisie != "" and not error_message:   # au final, on devrait obtenir une chaine vide
            error_message.add(f"enchainement {self.label.replace(test_saisie,"")} - {test_saisie} erroné")

        # export du résultat
        if error_message:
            return False, f"{self.label}: {", ".join(error_message)}"
        return True, ""

    def is_roman(self):
        valid, _ = self.validate_roman()
        return valid

    def get_anomaly(self):
        _, message = self.validate_roman()
        return message


    def get_roman_value(self) -> int:
        """ Retourne l'entier correspondant à la saisie romaine *ou un message d'erreur*"""
        # * voir comment provoquer une exception plutôt que retourner une chaine là où un entier est attendu *
        nombre = 0  # initialisation
        saisie = self.label
        # Pour clé dans le dictionnaire
        for key, valeur in ROMAN_DIGITS.items():
            # si clé correspond au début de saisie
            while saisie[0:len(key)] == key:
                nombre += valeur
                # effacer clé de saisie
                saisie = saisie[len(key):]
        return nombre if  self.validity else "Syntaxe romaine erronée"  # *à revoir*

    @staticmethod
    def roman_convert(nombre: int) -> str:
        """ Retourne la transcription romaine d'un nombre arabe"""
        roman = ""  # initialisation
        # pour valeur dans le dictionnaire
        for symbol, valeur in ROMAN_DIGITS.items():
            n = nombre // valeur
            roman = roman + symbol * n  # concaténer roman
            nombre -= n * valeur  # soustraire de nombre
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
    # test saisie romaine
    while True:
        guess = input("saisie nombre romain ou (Q) pour quitter: ")
        print(f"nom: {Roman(guess).label}")
        print(f"validité: {Roman(guess).validity}")
        print(f"anomalie: {Roman(guess).anomaly}")
        print(f"valeur: {Roman(guess).value}")
        if guess.upper() == "Q":
            break

    #test add_romans
    while True:
        print("ADDITIO ROMANA \n Saisissez des nombres romains séparés par un +")

        guess = input("saisie utilisateur ou (Q) pour quitter: ")
        if guess.upper() == "Q":
            exit()
        print(Roman.add_romans(guess))
