import requests


class SecretClient():
	def __init__(self, url: str = "http://127.0.0.1", port: str = '8000', path: str = ''):
		self.api_url = f'{url}:{port}{path}'

	def create_secret(self, data: dict):
		return requests.post(self.api_url + '/generate', data=data)

	def retrieve_secret(self, secret_key: str, data: dict):
		return requests.post(self.api_url + '/secret/' + secret_key, data=data)
