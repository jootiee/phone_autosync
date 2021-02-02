from server_connect import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface, self)
        self.ftp = FTP()
        self.main_windows.setCurrentIndex(0)

        self.button_assign()

    def button_assign(self):
        self.button_save.clicked.connect(self.save_credentials)
        self.button_upload.clicked.connect(self.ftp.upload) 
        self.button_download.clicked.connect(self.download_page)

    def save_credentials(self):
        ip = self.input_server_ip.text()
        username = self.input_server_ip.text()
        password = self.input_server_ip.text()

        if True:  # connection_attempt(ip, username, password):
            self.main_windows.setCurrentIndex(1)
        else:
            pass

        # rewrite(ip=ip, username=username, password=password)

    def download_page(self):
        self.main_windows.setCurrentIndex(2)
        self.ftp.download()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
