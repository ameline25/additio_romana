from time import sleep
import sys

class TuringMachina:
    def __init__(self, program: str, ribbon: str, end: str, t_index: int):
        """ Initialisation de la machine"""
        self.registry_state = "a"
        self.data_bus = ""
        self.memory_ribbon = ribbon
        self.turing_index = t_index
        self.turing_code = program
        self.end = end

    def print_activity(self):
        """Affiche l'état de machine ainsi que la position de la tête et le contenu du ruban mémoire.
           S représente l'état, n la position de la tête, x le contenu du ruban en lu

                State: S Read index: 00n début_ruban[x]fin_ruban
        """
        index= self.turing_index
        if index == 0:
            p_ribbon = f"[{self.memory_ribbon[index]}]{self.memory_ribbon[index + 1:]}"
        elif index == len(self.memory_ribbon):
            p_ribbon = f"{self.memory_ribbon[:index]}[{self.memory_ribbon[index]}]"
        else:
            p_ribbon = f"{self.memory_ribbon[:index]}[{self.memory_ribbon[index]}]{self.memory_ribbon[index + 1:]}"
        return f"State: {self.registry_state}  Read_index: {self.turing_index :03d} {p_ribbon}\n"

    def compute(self):
        """ Fonctionnement de la machine, boucle la lecture du ruban jusqu'à atteindre une condition de sortie."""
        index = self.t_index
        self.data_bus = self.memory_ribbon[index]
        # construction de la clé d'instruction
        key = self.registry_state + self.data_bus
        while self.registry_state not in self.end:
            # Exécuter les instructions selon les valeurs correspondant à la clé
            # écriture de w sur le ruban en position ou ne rien écrire si ""
            # ...à faire...

            # déplacement de la tête : à gauche pour "<", à droite pour ">", aucun si "" -> augmenter ou diminuer index
            # ...à faire...

            # modification de l'état
            # ...à faire...

            sys.stdout.write(self.print_activity())
            sys.stdout.flush()  # Force l'affichage immédiat
            sleep(0.33)

    def create_dictionary(self):
        """ Décompose le programme sous forme d'un dictionnaire {sr: wmn, }"""
        dic = {}
        i = 0
        while i+4 < len(self.turing_code):
            dic_key = self.turing_code[i: i+2]
            dic_value = self.turing_code[i+2 : i+5]
            dic[dic_key] = dic_value
            i += 5
        return dic


if __name__ == "__main__":
    #renseigne les conditions initiales
    ribbon = input("Indiquez le contenu du ruban mémoire: ")
    program = input("Indiquez les instructions de programmation: ")
    end = input("Indiquez les critères de sortie: ")
    index = int(input("Renseignez la position de la tête de lecture: "))
    # créé la machine

    machine = TuringMachina(program = program, ribbon = ribbon, end = end, t_index = index)
    machine.create_dictionary()
    machine.compute()




