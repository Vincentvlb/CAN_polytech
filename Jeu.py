
import threading
import serial

class Jeu:
    def __init__(self, port, resultat_capteur, resultat_jeu):
        self.__level = 0
        self.__busCan = serial.Serial(port = port, baudrate = 115200)
        self.__resultat_capteur = resultat_capteur
        self.__resultat_jeu = resultat_jeu
    
    def run():
        pass

    def exit_game():
        pass

    def getCan():
        pass