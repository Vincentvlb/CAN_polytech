from Capteur import Capteur

class Appui (Capteur):

    def traduction_IHM(self):
        valeur = int(self._valeur_voulue)
        return valeur
