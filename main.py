from server_connect import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect, Qt, QSize


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface, self)
        self.ftp = FTP()
        self.main_windows.setCurrentIndex(0)

        self.gallery_load()
        self.initUI()

    def initUI(self):
        self.button_save.clicked.connect(self.save_credentials)
        self.button_upload.clicked.connect(self.ftp.upload)
        self.button_download.clicked.connect(self.gallery_page)

    def save_credentials(self):
        ip = self.input_server_ip.text()
        username = self.input_server_ip.text()
        password = self.input_server_ip.text()

        attempt = True  # self.ftp.connection_attempt(ip, username, password)

        if attempt:
            self.main_windows.setCurrentIndex(1)
        else:
            print('wrong')
        # self.config_rewrite(ip=ip, username=username, password=password)

    def config_rewrite(self, ip, username, password):
        config.set('server', 'ip', ip)
        config.set('client', 'username', username)
        config.set('client', 'password', password)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def gallery_page(self):
        self.main_windows.setCurrentIndex(1)

    def gallery_load(self):
        self.gridLayoutWidget = QWidget(self.page_gallery)
        self.gridLayoutWidget.setGeometry(QRect(30, 10, 311, 10))
        self.gridLayoutWidget.setObjectName("layout_gallery")
        self.layout_gallery = QGridLayout(self.gridLayoutWidget)
        self.layout_gallery.setSizeConstraint(QLayout.SetFixedSize)
        self.layout_gallery.setContentsMargins(0, 0, 0, 0)
        self.layout_gallery.setVerticalSpacing(6)

        pictures = [os.path.join(upload_dir, picture)
                    for picture in os.listdir('upload')]
        row, column = 0, 0
        for index, image in enumerate(pictures):
            #TODO: remove it
            if index == 15:
                break
            self.pic = QPushButton(self.gridLayoutWidget)
            self.pic.setMaximumSize(QSize(99, 127))
            self.pic.setLayoutDirection(Qt.LeftToRight)
            self.pic.setAutoFillBackground(False)
            self.pic.setStyleSheet("background: rgba(255, 255, 255, 0.01)")
            self.pic.setText("")
            icon = QIcon()
            icon.addPixmap(QPixmap(image), QIcon.Normal, QIcon.Off)
            self.pic.setIcon(icon)
            self.pic.setIconSize(QSize(99, 127))
            self.pic.setFlat(False)
            self.pic.clicked.connect(self.gallery_page)
            self.pic.setObjectName("pic_" + str(index))
            self.layout_gallery.addWidget(self.pic, row, column, 1, 1)

            column += 1
            if column == 3:
                row += 1
                column = 0



    def picture_page(self, picture):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
