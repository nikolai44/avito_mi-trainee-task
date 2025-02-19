from pydantic import BaseModel, Field


class SecretInCreating(BaseModel):
	secret: str = Field(..., title='The value of the secret', min_length=1, max_length=10000)
	passphrase: str = Field(..., title='The passphrase for secret access', min_length=4, max_length=30)
	ttl: int = Field(None, gt=60, title='The ttl must be greater than 1 min')


class SecretInRetrieving(BaseModel):
	passphrase: str


class SecretOutCreating(BaseModel):
	secret_key: str


class SecretOutRetrieving(BaseModel):
	secret: str
