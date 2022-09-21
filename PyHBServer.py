import argparse
import logging
from time import sleep, strftime
from datetime import datetime, timedelta
import socket
import configparser

logging.basicConfig(format='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s', level = logging.DEBUG, datefmt='%H:%M:%S')

'''class BeatDict:
    def __init__(self):
        self.beat_dict = {}
    
    def update(self,ip):
        self.beat_dict[self,ip] = datetime.now()

    def checkTimeout(self,ip):
        self.delta = datetime.now() - self.beat_dict[ip]


class ServerSocket():
    def __init__(self,server,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server,self.port)

    def recv(self):
        data, addr = self.sock.recvfrom(10)
        logging.info('Recieved {} from {}'.format(data,addr))'''

def readConfig():
    config = configparser.ConfigParser()
    logging.debug('Reading configration file')
    config.read('config.ini')
    return config['HBServer']['host'], eval(config['HBServer']['port'])

def main():
    server, port = readConfig()
    logging.debug(f'Creating socket at {server} : {port}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    logging.debug('Socket Created')
    logging.debug(f'Binding to socket at {server} : {port}')
    sock.bind((server,port))
    logging.debug(f'Listening on socket at {server} : {port}')
    while 1:
        data, addr = sock.recvfrom(10)
        logging.info('Recieved Hello Packet from {} : {}'.format(addr[0], addr[1]))
        #sleep(2)

if __name__ == '__main__':
    logging.debug('Program Started')
    main()
