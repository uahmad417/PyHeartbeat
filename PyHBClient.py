import logging
from time import sleep
from datetime import datetime
import socket
import configparser



def readConfig():
    global config
    config = configparser.ConfigParser()
    config.read('config.ini')


if __name__ == '__main__':
    readConfig()
    logging.basicConfig(
        format ='%(asctime)s -- %(levelname)s -- %(threadName)s --  %(message)s',
        level = eval(config['Logging']['level']),
        filename = config['Logging']['file'],
        datefmt ='%H:%M:%S')
    logging.debug('Read configration file')
    logging.debug('Starting Program')
    logging.debug('Creating Socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    while 1:
        logging.info(f'PyHeartBeat client sending Hello packet to IP {config["HBServer"]["host"]} , port {eval(config["HBServer"]["port"])}')
        msg = f'Hello at _ {str(datetime.now())}'
        sock.sendto(msg.encode('utf-8'),(config['HBServer']['host'],eval(config['HBServer']['port'])))
        sleep(eval(config["HBClient"]["HBWait"]))