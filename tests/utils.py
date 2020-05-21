import random
import string
from client import SecretClient


def random_string(length):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def create_secret_random_data(secret_len=8, passw_len=8):
	secret = {
		'secret': random_string(secret_len),
		'passphrase': random_string(passw_len),
	}
	client = SecretClient()
	return client.create_secret(secret)
