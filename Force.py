from Capteur import Capteur

class Force (Capteur):
    
    def traduction_IHM(self):
        valeur = int(self._valeur_voulue)
        return valeur