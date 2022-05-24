from flask import Flask, render_template
import multiprocessing
from typing import Callable

class WebServer:

    def __init__(self, server_dir: str):
        self.__app = Flask("webserver")
        self.__app.add_url_rule('/', view_func=self.__index)

    def run_server(self, host: str, port: int):
        self.__webStream = multiprocessing.Process(target=self.__app.run, args=(host, port, False))
        self.__webStream.start()

    def __index(self):
        return render_template("index.html")