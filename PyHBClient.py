import argparse
import logging
from time import sleep, strftime
from datetime import datetime

parser = argparse.ArgumentParser(
    prog='PyHBClient.py',
    description='This is the heartbeat client'
)

parser.add_argument(
    '-ip',
    '--ip',
    help = 'The ip of the heartbeat server, defaults to localhost',
    type = str
)

parser.add_argument(
    '-p',
    '--port',
    help = 'The port of the heartbeat serer, defaults to 1234'
)

args = parser.parse_args()

logging.basicConfig(format = '%(asctime)s - %(message)s', level = logging.INFO)