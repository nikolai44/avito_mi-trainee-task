FROM python:3.7

WORKDIR /opt/project

COPY ./requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 22 8000

COPY ./app ./app
COPY ./tests ./tests
COPY ./run.py ./

CMD [ "python3", "./run.py" ]
