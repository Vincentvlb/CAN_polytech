from Capteur import Capteur

class Vitesse (Capteur):
    def _init(self):
        self._valeur_possible = ["Low","Fast"]

    def traduction_IHM(self):
        if(self._valeur_voulue == 0):
            valeur = self._valeur_possible[0]
        elif(self._valeur_voulue == 1):
            valeur = self._valeur_possible[1]
        return valeur