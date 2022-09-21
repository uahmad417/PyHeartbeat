import argparse
from concurrent.futures import thread
import logging
from time import sleep, strftime
from datetime import datetime, timedelta
import socket
import configparser
import threading
import concurrent.futures

logging.basicConfig(format='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s', level = logging.DEBUG, datefmt='%H:%M:%S')

class BeatDict:
    def __init__(self):
        logging.debug('Creating dictionary to store HeartBeat Clients')
        self.beat_dict = {}

    def update_dict(self,ip,recieve_time):
        self.beat_dict[ip] = recieve_time
    
    def check_hbclient_health(self):
        if len(self.beat_dict) != 0:
            for ip, timestamp in self.beat_dict.items():
                logging.info(f'Heart Beat Client at IP {ip} is alive')\
                    if (datetime.now()-datetime.strptime(timestamp.strip(),'%Y-%m-%d %H:%M:%S.%f')).seconds < 30\
                    else logging.warning(f'HeartBeat client at {ip} is dead')
        else:
            logging.info('No Heartbeat clients connected yet')

class BeatRec(BeatDict):
    def __init__(self, server, port):
        super(BeatRec,self).__init__()
        logging.debug(f'Creating socket at {server} : {port}')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        logging.debug('Socket Created')
        logging.debug(f'Binding to socket at {server} : {port}')
        self.sock.bind((server,port))
        logging.debug(f'Listening on socket at {server} : {port}')
    
    def recieve(self,event):
        while event.is_set():
            data, addr = self.sock.recvfrom(50)
            logging.info('Recieved Hello Packet from {} : {}'.format(addr[0], addr[1]))
            self.update_dict(addr[0],data.decode('utf-8').split('_')[1])


def readConfig():
    config = configparser.ConfigParser()
    logging.debug('Reading configration file')
    config.read('config.ini')
    return config

def main():
    config = readConfig()
    beat_recieve = BeatRec(config['HBServer']['host'], eval(config['HBServer']['port']))
    
    logging.debug('Creating Thread Event')
    event = threading.Event()
    logging.debug('Creating Thread')
    beat_thread = threading.Thread(target=beat_recieve.recieve,args=[event])
    logging.debug('Setting the thread event')
    event.set()
    logging.debug('Starting the thread')
    beat_thread.start()
    while 1:
        logging.debug('Sleeping for 10 secs...')
        sleep(10)
        logging.debug('Clearing the thread event')
        event.clear()
        beat_recieve.check_hbclient_health()
        event.set()

if __name__ == '__main__':
    logging.debug('Program Started')
    main()
