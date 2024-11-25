from time import sleep
import sys

class TuringMachina:
    def __init__(self, program: str, ribbon: str, end: str, t_index: int):
        """ Initialisation de la machine"""
        self.registry_state = "a"
        self.data_bus = ""
        self.memory_ribbon = ribbon
        self.t_index = t_index
        self.program = program
        self.end = end

    def print_activity(self, t_index: int):
        """Affiche l'état de machine ainsi que la position de la tête et le contenu du ruban mémoire.
           S représente l'état, n la position de la tête, x le contenu du ruban en lu

                State: S Read index: 00n début_ruban[x]fin_ruban
        """
        p_ribbon = f"{self.memory_ribbon[:t_index]}[{self.memory_ribbon[t_index]}]{self.memory_ribbon[t_index + 1:]}"
        return f"State: {self.registry_state}  Read_index: {t_index :0f3} {p_ribbon}"

    def compute(self):
        """ Fonctionnement de la machine, boucle la lecture du ruban jusqu'à atteindre une condition de sortie."""
        t_index = self.t_index
        self.data_bus = self.memory_ribbon[t_index]
        # construction de la clé d'instruction
        key = self.registry_state + self.data_bus
        while self.registry_state not in machine.end:
            # Exécuter les instructions selon les valeurs correspondant à la clé
            # écriture
            # ...à faire...

            # déplacement de la tête
            # ...à faire...

            # modification de l'état
            # ...à faire...

            sys.stdout.write(print_activity(self, t_index))
            sys.stdout.flush()  # Force l'affichage immédiat
            sleep(0.33)


if __name__ == "__main__":
    # créé la machine
    machine = TuringMachina
    #renseigne les conditions initiales
    machine.memory_ribbon = input("Indiquez le contenu du ruban mémoire: ")
    machine.program = input("Indiquez les instructions de programmation: ")
    # décomposer les instructions sous forme d'un dictionnaire {sr: wmn, }
    # ...à faire...

    machine.end = input("Indiquez les critères de sortie: ")
    machine.index = int(input("Renseignez la position de la tête de lecture: "))

    compute(machine)




