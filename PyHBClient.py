import argparse
import logging
from time import sleep, strftime
from datetime import datetime
import socket
import configparser

logging.basicConfig(format='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s', level = logging.DEBUG, datefmt='%H:%M:%S')

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