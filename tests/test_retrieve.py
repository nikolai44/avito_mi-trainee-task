from client import SecretClient


def test_retrieve_basic():
	client = SecretClient()
	data = {
		"secret": "test",
		"passphrase": "123123123"
	}
	r = client.create_secret(data)
	secret_key = r.json()['secret_key']
	r = client.retrieve_secret(secret_key, data)
	assert 'secret' in r.json()
	assert r.json()['secret'] == data['secret'], 'sent and retrieved secret not the same'
	assert r.status_code == 200, 'status code incorrect'
	r = client.retrieve_secret(secret_key, data)
	assert r.status_code == 404, 'after first retrieve secret should be deleted'


def test_retrieve_notexisting():
	client = SecretClient()
	secret = {
		'passphrase': '123123123'
	}
	valid_object_id = 'dddddddddddddddddddddddd'
	r = client.retrieve_secret(valid_object_id, secret)
	assert r.status_code == 404


def test_retrieve_empty_json():
	client = SecretClient()
	data = {
		"secret": "test",
		"passphrase": "123123123"
	}
	r = client.create_secret(data)
	r = client.retrieve_secret(secret_key=r.json()['secret_key'], data='')
	assert r.status_code == 422
