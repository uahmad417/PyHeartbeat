import logging
from time import sleep
from datetime import datetime
import socket
import configparser
import threading

class BeatDict:
    def __init__(self):
        logging.debug('Creating dictionary to store HeartBeat Clients')
        self.beat_dict = {}

    def update_dict(self,ip,recieve_time):
        logging.debug(f'Client Dictionary Updated with IP {ip}')
        self.beat_dict[ip] = recieve_time
    
    def check_hbclient_health(self):
        if len(self.beat_dict) != 0:
            for ip, timestamp in self.beat_dict.items():
                logging.info(f'Heartbeat Client at IP {ip} is alive')\
                    if (datetime.now()-datetime.strptime(timestamp.strip(),'%Y-%m-%d %H:%M:%S.%f')).seconds < 30\
                    else logging.warning(f'HEARTBEAT CLIENT AT {ip} IS DEAD')
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
            logging.info('Recieved Heartbeat from {} : {}'.format(addr[0], addr[1]))
            self.update_dict(addr[0],data.decode('utf-8').split('_')[1])


def readConfig():
    global config
    config = configparser.ConfigParser()
    config.read('config.ini')

def main():
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
        sleep(eval(config["HBServer"]["check_health"]))
        logging.debug('Clearing the thread event')
        event.clear()
        beat_recieve.check_hbclient_health()
        event.set()

if __name__ == '__main__':
    readConfig()
    logging.basicConfig(
        format='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s',
        level = eval(config['Logging']['level']),
        filename=config['Logging']['file'],
        datefmt='%H:%M:%S')
    logging.debug('Read Configuration File')
    logging.debug('Program Started')
    main()
