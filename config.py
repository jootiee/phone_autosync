import os
import sys
import ftplib
import requests
from compression import *
from configparser import ConfigParser
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect, Qt, QSize

current_dir = os.path.dirname(__file__)

interface = os.path.join(current_dir, "ui/interface.ui")

config = ConfigParser()
config.read('config.ini')


try:
    gallery_dir = os.path.join(current_dir, 'gallery')
except:
    os.mkdir('gallery')
    gallery_dir = os.path.join(current_dir, 'gallery')


server_dir = config['server']['folder']

ip = config['server']['ip']
username = config['client']['username']
password = config['client']['password']
if int(config['client']['firstrun']):
    first_run = True
else:
    first_run = False

def get_paths(FTP):
    paths = list()
    for path in FTP.nlst():
        path = path[::-1][:path[::-1].index("/")][::-1]
        paths.append(path)
    return paths
