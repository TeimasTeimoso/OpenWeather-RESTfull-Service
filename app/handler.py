
from http.server import BaseHTTPRequestHandler
import api, json

class RequestHandler(BaseHTTPRequestHandler):

	def __init__(self, request, client_address, server):
	 super().__init__(request, client_address, server)
	 # initialize api when creating the request handler
	 api.init()

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','application/json; charset=utf-8')
		self.end_headers()
		response = self.process_request()
		self.wfile.write(json.dumps(response).encode())

	def process_request(self):
		if self.path.startswith("/weather/city/"):
			# partition returns a 3 part tuple
			city_id = self.path.partition("/weather/city/")[2]
			return api.get_weather(city_id)
		else:
			print("FINITY")

