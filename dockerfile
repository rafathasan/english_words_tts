FROM python:3.11-slim-buster

RUN adduser --system --group --no-create-home -u 1000 docker

RUN mkdir /app && chown docker /app

RUN pip install gTTS

RUN apt update -y && \
apt install pulseaudio -y && \
apt install mpg321 -y && \
apt autoclean

WORKDIR /app

COPY ./main.py ./words.txt /app

USER docker

ENTRYPOINT ["python", "main.py"]
