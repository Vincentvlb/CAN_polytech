from Capteur import Capteur

class Position (Capteur):
    def _init(self):
        self._valeur_possible = ["Nord", "Sud", "Est", "Ouest"]

    def traduction_IHM(self):
        if (self._valeur_voulue == 1):
            valeur = self._valeur_possible[2]
        elif (self._valeur_voulue == 2):
            valeur = self._valeur_possible[3]
        elif (self._valeur_voulue == 3):
            valeur = self._valeur_possible[1]
        elif (self._valeur_voulue == 4):
            valeur = self._valeur_possible[0]
        return valeur