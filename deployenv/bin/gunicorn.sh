#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/hello.log
LOGDIR=/var/log/gunicorn/
NUM_WORKERS=3
# user/group to run as
USER=root
GROUP=root
cd /srv/www/backend/backend
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -b 0.0.0.0:80 backend.wsgi:application -w $NUM_WORKERS --timeout 3000
    --user=$USER --group=$GROUP --log-level=debug -
    --log-file=$LOGFILE 2>>$LOGFILE
