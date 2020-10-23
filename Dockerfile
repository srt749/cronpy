FROM python:3.8-slim-buster

# Install cron
RUN apt-get update && apt-get -y install cron
RUN apt-get update && apt-get install -y dos2unix

# Add crontab file (from your windows host) to the cron directory
ADD cron-test /etc/cron.d/hello-cron
COPY main.py /home
COPY job.sh /home

# Change line ending format to LF
RUN dos2unix /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron
RUN chmod 0744 /home/main.py
# RUN chmod 0755 /home/main.py
# RUN chmod +x /home/main.py
RUN chmod +x /home/job.sh

# Setup cron job
# RUN (crontab -l ; "* * * * * python home/main.py") | crontab
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log 
RUN touch /var/log/main.log 

# Run the command on container startup
# CMD ["crond", "-f", "-d", "8"]
# CMD cron start && tail -f /var/log/main.log
ENTRYPOINT cron start && tail -f /var/log/cron.log
# ENTRYPOINT ["bin/bash"]
# CMD python home/main.py

# Here you can put cmd for cron job for python file main.py
# To start:  docker run -i -t python:3.8-slim-buster