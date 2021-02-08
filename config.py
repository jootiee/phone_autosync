import os
import sys
import ftplib
import requests
from compression import *
from configparser import ConfigParser

current_dir = os.path.dirname(__file__)

interface = os.path.join(current_dir, "ui/interface.ui")

config = ConfigParser()
config.read('config.ini')

upload_dir = os.path.join(current_dir, 'upload')
download_dir = os.path.join(current_dir, 'download')
server_dir = config['server']['folder']

ip = config['server']['ip']
username = config['client']['username']
password = config['client']['password']


run = False
# while True:
    # if run:
        # gallery = [self.pic_0,
                #    self.pic_1,
                #    self.pic_2,
                #    self.pic_3,
                #    self.pic_4,
                #    self.pic_5,
                #    self.pic_6,
                #    self.pic_7,
                #    self.pic_8,
                #    self.pic_9,
                #    self.pic_10,
                #    self.pic_11,
                #    self.pic_12,
                #    self.pic_13,
                #    self.pic_14]
        # break



def current_dir_contains(FTP):
    paths = list()
    for path in FTP.nlst():
        path = path[::-1][:path[::-1].index("/")][::-1]
        paths.append(path)
    return(paths)
