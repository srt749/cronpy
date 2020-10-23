##!/usr/local/bin python

import logging

logging.FileHandler(
    filename='/var/log/main.log',
    mode='w', 
    encoding=None, 
    delay=False)

logging.basicConfig(
    level=logging.DEBUG, 
    format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))

print('hello')

logging.debug('End of program')

# Try to write a log file, maybe with logging module
# logging module: https://automatetheboringstuff.com/2e/chapter11/
# Set up a Docker volume, in the run command