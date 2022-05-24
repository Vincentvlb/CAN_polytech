
import threading
import serial
import time
# from Capteur import capteur
# from Couleur import couleur
# from Position import position
# from Force import force
# from Vitesse import vitesse
# from Appui import appui

__lock = threading.Lock()

class Jeu:
    def __init__(self, port):
        self.__level = 0
        self.__busCan = serial.Serial(port = port, baudrate = 115200)
        self.__listeTaches = []
        self.__listeCapteur = []
        self.__listeTrame = []
        self.__indexAction = 0
        #self.__resultat_capteur = resultat_capteur
        #self.__resultat_jeu = resultat_jeu
        

    def initCapteur():
        self.__listeCapteurs.append(Position())
        self.__listeCapteurs.append(Appui())
        self.__listeCapteurs.append(Force())
        self.__listeCapteurs.append(Vitesse())
        self.__listeCapteurs.append(Couleur())

    def run(self):
        
        self.__lock = threading.Lock()
        print("lock ok ")
        arret_jeu = True
        arret_manche = True
        cptAct = 0

        #self.__busCan.open()
        thread_incoming_message = threading.Thread(target=self.process_incoming_message)
        thread_incoming_message.start()

        
        __level = 0

        while arret_jeu:

            __level += 1

            while arret_manche:

                if self.__listeTrame:
                    self.__lock.acquire()
                    tmpTrame = self.__listeTrame.pop()
                    self.__lock.release()
                    if check_action(tmpTrame):
                        cptAct += 1
                    else:
                        arret_manche = False

                if cptAct == len(self.__listeTaches):
                    arret_manche = False
            
            self.__indexAction = 0
                
        thread_incoming_message.close()
        exit_game()

    def getAction(self):
        pass
        # capteur = randint(0,5)
        # if capteur == 0:
        #     __listeTaches.append(couleur())
        # elif capteur == 1:
        #     __listeTaches.append(force())
        # elif capteur == 2:
        #     __listeTaches.append(vitesse())
        # elif capteur == 3:
        #     __listeTaches.append(position())
        # elif capteur == 4:
        #     __listeTaches.append(appui())
        #elif capteur == 5:
        #    __listeTaches.append(couleur())
        
    def check_action(self, trame):
        print("check action")
        valeurRecup = trame[4:9]
        print(valeurRecup)

        #if __listeCapteurs[trame[1:2]-1].get_valeur_voulu == trame[8:9]

        #self.__indexAction+=1


        

    def exit_game(self):
        self.__busCan.close()

    def send_data(self):
        pass
    
    def process_incoming_message(self):
        print("thread")
        while 1:
            retourBus = self.__busCan.read(10)
            print(retourBus)
            self.__lock.acquire()
            self.__listeTrame.append(retourBus[3:9])  
            self.__lock.release()
            time.sleep(0.1)

if __name__ == '__main__':
    jeu = Jeu("COM7")
    jeu.run()
