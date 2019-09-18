FROM python:3.7-alpine

COPY . ./client

WORKDIR /client

RUN pip install -r requirements.txt

CMD python client.py