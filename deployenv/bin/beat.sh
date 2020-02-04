#!/bin/bash
useradd celeryuser

export C_FORCE_ROOT=TRUE

startBeat(){
    cd /srv/www/backend/backend
    celery -A backend beat
}

startBeat
