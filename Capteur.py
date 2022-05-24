class Capteur:
    def __init__(self,_id,_valeur_voulue):
        self._id = _id
        self._valeur_voulue = _valeur_voulue
        

    def traduction_IHM():
        pass

    def get_id(self):
        return self._id
    
    def get_valeur_voulue(self):
        return self._valeur_voulue