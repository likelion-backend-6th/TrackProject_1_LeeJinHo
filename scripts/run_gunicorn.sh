#!/bin/bash

# 실행 경로 진입
cd /home/lion/twitter/twitter
# activate venv
source /home/lion/twitter/venv/bin/activate
# gunicorn 실행
gunicorn twitter.wsgi:application --config twitter/gunicorn_config.py