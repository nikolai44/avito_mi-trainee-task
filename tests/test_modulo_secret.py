import sys
sys.path.append("./../app")
from app.secret import crypt_secret, decrypt_secret, save_secret_to_db,\
	get_secret_by_objectid, delete_secret_by_objectid
from app.models import SecretInCreating


def test_decrypt_secret():
	secret = SecretInCreating(secret='test', passphrase='test')
	crypted_secret = {
		'salt': '$2b$12$ft0vF0R9o1OOK9BnfLnvxe',
		'hashed_passphrase': '$2b$12$CUdjXoPQrNkz2Bhc9Nqz2eEOUfe8gxBQGDdC2L1zgakcSswdj2sJ.',
		'crypted_secret': b'4YVh6gx1kGmA+Id0g/9CZtdO3Z67jsy1x1aXcPIqebw='
	}
	decrypted_secret = decrypt_secret(crypted_secret, secret.passphrase)
	assert secret.secret == decrypted_secret['secret']


def test_crypt_secret():
	secret = SecretInCreating(secret='test', passphrase='test')
	decrypted_secret = decrypt_secret(crypt_secret(secret), secret.passphrase)
	assert secret.secret == decrypted_secret['secret']
