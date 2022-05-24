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


def main():
    webServer = WebServer()
    webServer.run_server("0.0.0.0", 80)
    while True :
        webServer.socketio.emit('ihm', {"joystick":"N"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"btn":"Rouge"} , namespace='/ihm')
        time.sleep(1)
        webServer.socketio.emit('ihm', {"btn":"Bleu"} , namespace='/ihm')
        time.sleep(1)

if __name__ == "__main__":
    main()