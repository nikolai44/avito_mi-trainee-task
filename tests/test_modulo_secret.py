from secret import crypt_secret, decrypt_secret, save_secret_to_db,\
	get_secret_by_objectid, delete_secret_by_objectid
from models import SecretInCreating

'''
def test_crypt_secret():
	secret_data = {
		"secret": "test",
		"passphrase": "123123123"
	}
	secret = SecretInCreating(secret_data)
	secret.secret = 'test'
	secret.passphrase = '123123123'
	crypted_secret = crypt_secret(secret)
	assert crypted_secret == True


test_crypt_secret()
'''
