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


def rewrite(ip, username, password):
    config.set('server', 'ip', ip)
    config.set('client', 'username', username)
    config.set('client', 'password', password)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def current_dir_contains(FTP):
    paths = list()
    for path in FTP.nlst():
        path = path[::-1][:path[::-1].index("/")][::-1]
        paths.append(path)
    return(paths)