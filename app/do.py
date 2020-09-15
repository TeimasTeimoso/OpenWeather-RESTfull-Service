#system imports
import os
import sys
import toml
from http.server import HTTPServer

#local imports
from handler import RequestHandler, api

server_config = toml.load("config/config.toml")["server"]

# initialize api when creating the server handler
api.init()
server = HTTPServer((server_config["host"], server_config["port"]), RequestHandler)
server.serve_forever()