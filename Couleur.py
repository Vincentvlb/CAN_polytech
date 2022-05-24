from Capteur import Capteur

class Couleur (Capteur):
    def _init(self):
        self._valeur_possible = ["Rouge", "Blanc", "Vert", "Bleu"]

    def traduction_IHM(self):
        if (self._valeur_voulue == 2): 
            valeur = self._valeur_possible[1]
        elif (self._valeur_voulue == 3):
            valeur = self._valeur_possible[0]
        elif (self._valeur_voulue == 4):
            valeur = self._valeur_possible[2]
        else :
            valeur = self._valeur_possible[3]
        return valeur