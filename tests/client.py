import requests


class SecretClient():
	def __init__(self, url: str = "http://127.0.0.1", port: str = '8000', path: str = ''):
		self.api_url = f'{url}:{port}{path}'
		self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

	def create_secret(self, data):
		return requests.post(self.api_url + '/generate', json=data, headers=self.headers)

	def retrieve_secret(self, secret_key: str, data):
		return requests.post(self.api_url + '/secret/' + secret_key, json=data, headers=self.headers)
