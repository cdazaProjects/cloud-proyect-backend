#!/bin/bash
useradd celeryuser

USER=celeryuser
GROUP=celeryuser
export C_FORCE_ROOT=TRUE

startCelery(){
    cd /srv/www/backend/backend
    celery -A backend worker -P eventlet -l info -n worker1@%h --concurrency=2 &
     celery -A backend worker -P eventlet -l info -n worker2@%h --concurrency=2  &
     celery -A backend beat
}

startCelery