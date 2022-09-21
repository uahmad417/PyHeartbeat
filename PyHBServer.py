import argparse
import logging
from time import sleep, strftime
from datetime import datetime, timedelta
import socket
import configparser

logging.basicConfig(format = '%(asctime)s - %(message)s', level = logging.INFO)

class BeatDict:
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
        logging.info('Recieved {} from {}'.format(data,addr))

def readConfig():
    config = configparser.ConfigParser()
    logging.info('Reading configration file')
    config.read('HBClient.ini')
    return config['HBServer']['host'], eval(config['HBServer']['port'])

def main():
    server, port = readConfig()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server,port))
    while 1:
        data, addr = sock.recvfrom(10)
        logging.info('Recieved {} from {}'.format(data,addr))
        print(dir(addr))
        sleep(2)

if __name__ == '__main__':
    main()
