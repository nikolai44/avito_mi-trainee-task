## Описание:
- Асинхронный web api сервис на python3.7
- В качестве фреймворка используется fastapi с сервером uvicorn
- В качестве базы данных использована mongodb с асинхронным драйвером motor
- Пароли хешируются с помощью bcrypt, секреты шифруются с помощью aes из из модуля pycrypto
- Для тестирования используется pytest и requests
- Для документации api используется Swagger
- Развёртывание с помощью docker
- [ТЗ на проект](ТЗ.md)

## Запуск:
	```
	git clone
	```
### Docker:
	```
	docker-compose up
	```
### Тесты:
	```bash
	pytests --cov=app tests/
	```
### Запуск локально 
	```
	# create database
	## start mongo
	systemctl start mongod
	## create admin if not exist
	mongo
	use admin
	db.createUser(
	  {
	    user: "admin
	    pwd: passwordPrompt(), // or cleartext password
	    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
	  }
	)
	ctrl+c
	## create user
	mongo --port 27017  --authenticationDatabase "admin" -u "admin" -p
	use admin
	db.createUser(
		{
		    user: "user",
		    pwd: "admin",
		    roles: [
		        {
		            role: "readWrite",
		            db: "fastapi"
		        }
		    ]
		}
	);
	
	python3.7 venv venv
	source venv/bin/activate
	pip3 install -r requirements.dev.txt
	python3 run.py
	pytests --cov=app tests/
	```
