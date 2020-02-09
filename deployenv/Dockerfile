FROM ubuntu:18.04



RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get update -y && \
  apt-get upgrade -y && \
  apt-get install -yf build-essential git ffmpeg  python3.5 python3-dev python3-pip binutils postgresql-server-dev-10 libnss3 tzdata netcat curl nano

COPY requirements.txt /tmp/requirements.txt

ARG CACHEBUST=1

RUN pip3 install pip==9.0.3 --upgrade && \
    pip3 install -r  /tmp/requirements.txt

RUN mkdir -p /srv/www/backend

ADD . /srv/www/backend
COPY bin /srv/www/bin
WORKDIR /srv/www/backend
RUN mkdir /srv/www/backend/celery-state
RUN chmod +x /srv/www/bin/*.sh

EXPOSE 80

CMD ["uwsgi", "--yaml", "/srv/www/backend/bin/uwsgi.yaml"]