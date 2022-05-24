from flask import Flask, render_template
import threading

class WebServer:

    def __init__(self):
        self.__app = Flask("webserver", static_folder="./templates")
        self.__app.add_url_rule('/', view_func=self.__index)

    def run_server(self, host: str, port: int):
        self.__webStream = threading.Thread(target=self.__app.run, args=(host, port, False))
        self.__webStream.start()

    def __index(self):
        return render_template("index.html")


def main():
    webServer = WebServer()
    webServer.run_server("0.0.0.0", 80)

if __name__ == "__main__":
    main()