FROM hoangph3/facekyc-webcam-js:x86_64-1.0.0

WORKDIR /app

COPY . .

RUN apt-get update -y && apt-get install nano telnet vim curl net-tools -y

RUN pip3 install -U pip && pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
