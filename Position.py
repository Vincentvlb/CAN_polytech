from Capteur import Capteur

class Position (Capteur):
    
    def traduction_IHM(self):
        valeur = str(self._valeur_voulue)
        return valeur