# cronpy

Simple dockerized-cron-python script with retained log file

Runs every minute, logs from python module to local log.log via docker volume

## commands

>>> docker build -t cronpy .

(Replace .\ with your local path:)
>>> docker run -it -v .\cronpy\log.log:/var/log/cron.log cronpy
