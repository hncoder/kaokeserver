#/bin/bash


#!/bin/sh
#You Can set the program name and config file name below:

echo 'Starting...'

source venv/bin/activate

cd kaokeadmin
#nohup python3 manage.py runserver -h 0.0.0.0 &
nohup gunicorn -w 4 -b 127.0.0.1:8081 manage:app &
