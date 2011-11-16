#!/bin/bash

approot="`pwd`/`dirname "$0"`/../../"

export PYTHONPATH=$approot/src:${PYTHONPATH}

COMPASSPATH=$approot/compass/
pushd $COMPASSPATH
killall compass
compass watch config &
COMPASS_PID=$!
popd

pushd  $approot/src/kluster/
../../../kluster-env/bin/python manage.py runserver app.dev:8000 --settings=kluster.settings
popd
