FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN apt-get update -y && apt-get install nano telnet vim curl net-tools -y

RUN pip3 install -U pip && pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
