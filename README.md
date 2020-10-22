# cronpy
Simple dockerized-cron-python script with retained log file

## commands

>>> docker build -t cron .

(Customize local logging path:)
>>> docker run -it -v .\logging.log:/var/log/cron.log cron
