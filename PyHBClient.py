import argparse
import logging
from time import sleep, strftime
from datetime import datetime
import socket
import configparser

logging.basicConfig(format='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s', level = logging.DEBUG, datefmt='%H:%M:%S')

'''def cli():
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
    return hb_server, hb_port'''

def readConfig():
    config = configparser.ConfigParser()
    logging.info('Reading configration file')
    config.read('HBClient.ini')
    return config['HBServer']['host'], eval(config['HBServer']['port'])


if __name__ == '__main__':
    server, port = readConfig()
    logging.info('Creating Socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    logging.info(f'PyHeartBeat client sending Hello packet to IP {server} , port {port}')
    while 1:
        sock.sendto('Hello'.encode('utf-8'),(server,port))
        sleep(5)