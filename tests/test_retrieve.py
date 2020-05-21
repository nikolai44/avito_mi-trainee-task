from client import SecretClient
from utils import create_secret_random_data


def test_retrieve_basic():
	client = SecretClient()
	data = {
		"secret": "test",
		"passphrase": "123123123"
	}
	r = client.create_secret(data)
	print(r.json)
	r = client.retrieve_secret(secret_key=r.json()['secret_key'], data=data)
	print(r.json)
	assert r.json()['secret'] == data['secret'], 'sent and retrieved secret not the same'


def test_retrieve_notexisting():
	client = SecretClient()
	secret = {
		'passphrase': '123123123'
	}
	valid_object_id = 'dddddddddddddddddddddddd'
	r = client.retrieve_secret(valid_object_id, secret)
	assert r.status_code == 404


def test_retrieve_invalid_json():
	pass


def test_retrieve_empty_json():
	pass


def test_retrieve_empty_query():
	pass
