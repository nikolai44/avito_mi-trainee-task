from os import urandom
from client import SecretClient


def create_secret_random_data(secret_len=8, passw_len=8):
	secret = {
		'secret': urandom(secret_len),
		'passphrase': urandom(passw_len),
	}
	client = SecretClient()
	return client.create_secret(secret)


def test_create_passw_range():
	down_range_pass = 4
	up_range_pass = 30

	for passw_len in range(32):
		r = create_secret_random_data(passw_len=passw_len)
		print(r.json())
		if down_range_pass <= passw_len <= up_range_pass:
			assert r.status_code == 200
		else:
			assert r.status_code == 422


def test_create_secret_range():
	down_range_secret = 1
	up_range_secret = 10000

	for secret_len in [0, 1, 10, 100, 10000, 10001]:
		r = create_secret_random_data(secret_len=secret_len)
		if down_range_secret <= secret_len <= up_range_secret:
			assert r.status_code == 200
		else:
			assert r.status_code == 422


def test_create_empty_passw():
	pass


def test_create_empty_secret():
	pass


def test_create_empty_json():
	pass


def test_create_empty_query():
	pass


def test_create_invalid_json():
	pass


def test_retrieve_notexisting():
	pass


def test_retrieve_morethanonce():
	pass


def test_retrieve_invalid_json():
	pass


def test_retrieve_empty_json():
	pass


def test_retrieve_empty_query():
	pass
