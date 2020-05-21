from client import SecretClient
from utils import create_secret_random_data


def test_create_passw_range():
	down_range_pass = 4
	up_range_pass = 30

	for passw_len in range(32):
		r = create_secret_random_data(passw_len=passw_len)
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


def test_create_empty_json():
	client = SecretClient()
	r = client.create_secret({})
	assert r.status_code == 422


def test_create_empty_query():
	client = SecretClient()
	r = client.create_secret('')
	assert r.status_code == 422

