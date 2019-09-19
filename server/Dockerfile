FROM python:3.7-alpine

COPY . ./server

WORKDIR /server

RUN pip install -r requirements.txt

VOLUME /var/server

EXPOSE 5151

CMD python server.py