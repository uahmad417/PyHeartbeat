import argparse
import logging
from time import sleep, strftime
from datetime import datetime, timedelta
import socket

logging.basicConfig(format = '%(asctime)s - %(message)s', level = logging.INFO)

class BeatDict:
    def __init__(self):
        self.beat_dict = {}
    
    def update(self,ip):
        self.beat_dict[self,ip] = datetime.now()

    def checkTimeout(self,ip):
        self.delta = datetime.now() - self.beat_dict[ip]

def cli():
    parser = argparse.ArgumentParser(
        prog='PyHBClient.py',
        description='This is the heartbeat client'
    )

    parser.add_argument(
        '-ip',
        '--ip',
        help = 'The interface on which the heartbeat server is listening, defaults to localhost',
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
    return hb_server, hb_port

class ServerSocket():
    def __init__(self,server,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server,self.port)

    def recv(self):
        data, addr = self.sock.recvfrom(10)
        logging.info('Recieved {} from {}'.format(data,addr))

def main():
    server, port = cli()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server,port))
    while 1:
        data, addr = sock.recvfrom(10)
        logging.info('Recieved {} from {}'.format(data,addr))
        print(dir(addr))
        sleep(2)
if __name__ == '__main__':
    main()
