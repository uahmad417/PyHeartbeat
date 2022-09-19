import argparse
import logging
from time import sleep, strftime
from datetime import datetime
import socket

logging.basicConfig(format = '%(asctime)s - %(message)s', level = logging.INFO)

parser = argparse.ArgumentParser(
    prog='PyHBClient.py',
    description='This is the heartbeat client'
)

parser.add_argument(
    '-ip',
    '--ip',
    help = 'The ip of the heartbeat server, defaults to localhost',
    type = str,
)

parser.add_argument(
    '-p',
    '--port',
    help = 'The port of the heartbeat serer, defaults to 1234'
)

args = vars(parser.parse_args())

hb_server = args['ip'] if args['ip'] is not None else '127.0.0.1'
hb_port = args['port'] if args['port'] is not None else 1234

logging.debug('Creating Socket')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logging.info('PyHeartBeat client sending to IP %s , port %d'%(hb_server, hb_port))
while 1:
    sock.sendto(b'Umair',(hb_server,hb_port))
    sleep(5)