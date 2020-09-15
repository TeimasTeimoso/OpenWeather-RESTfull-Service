#system imports
import os
import sys
import toml
from http.server import HTTPServer

#local imports
from handler import RequestHandler

server_config = toml.load("config/config.toml")["server"]

server = HTTPServer((server_config["host"], server_config["port"]), RequestHandler)
server.serve_forever()