from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

class WebServer:

    def __init__(self):
        self.__app = Flask("webserver")
        self.socketio = SocketIO(self.__app, async_mode=None, logger=False, engineio_logger=False)
        self.__app.add_url_rule('/', view_func=self.__index)

    def run_server(self, host: str, port: int):
        self.__webStream = threading.Thread(target=self.__app.run, args=(host, port, False))
        self.__webStream.start()

    def __index(self):
        return render_template("index.html")

    def resultat_capteur():
        pass

    def resultat_jeu():
        pass

def main():
    webServer = WebServer()
    webServer.run_server("0.0.0.0", 80)
    while True :
        webServer.socketio.emit('ihm', {"joystick":"N"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"joystick":"S"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"joystick":"E"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"joystick":"O"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"btn":"Appuyez"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"couleur":"Blanc"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"couleur":"Rouge"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"couleur":"Vert"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"couleur":"Bleu"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"vitesse":"Lent"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"vitesse":"Rapide"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"force":50} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"force":20} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"msg_look":True} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"msg_look":False} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"msg_look":True} , namespace='/ihm')
        time.sleep(1)

if __name__ == "__main__":
    main()