#!/bin/bash

cd /root/notouch/sterioms/  # Change to your project directory
source venv/bin/activate

pip3 install -r requirements.txt

export $(cat .env | xargs)

python3 manage.py collectstatic --no-input
python3 manage.py dumpdata core > data_backup.json
python3 manage.py migrate core

exec gunicorn sterioms.wsgi:application --bind 127.0.0.1:8006 --workers 4
deactivate