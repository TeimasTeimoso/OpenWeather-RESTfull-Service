
from http.server import HTTPServer, BaseHTTPRequestHandler

#Defining a HTTP request Handler class
#class ServiceHandler(BaseHTTPRequestHandler):
#
#	def do_GET(self):
#    	print("a")
#
#Server Initialization
#server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
#server.serve_forever()
class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.process_request()

	def process_request(self):
		if self.path.startswith("/weather/city/"):
			print("SENSE")
		else:
			print("FINITY")


server = HTTPServer(("localhost", 8080), RequestHandler)
server.serve_forever()