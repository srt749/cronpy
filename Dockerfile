FROM python:3.8-slim-buster

# Install cron / dos2unix
RUN apt-get update \ 
    && apt-get -y install cron \
    && apt-get install -y dos2unix 

# Add crontab file (from your windows host) to the cron directory
ADD cron-test /etc/cron.d/hello-cron
COPY main.py /home

# Change line ending format to LF
RUN dos2unix /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron \
    && chmod 0744 /home/main.py

# Setup cron job
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log 

# Run the command on container startup
ENTRYPOINT cron start && tail -f /var/log/cron.log