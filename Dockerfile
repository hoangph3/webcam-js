FROM python:3.7-slim

COPY . .

RUN apt-get update -y && apt-get install nano telnet vim curl net-tools -y

CMD [ "python3", "main.py" ]
