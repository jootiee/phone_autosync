from server_connect import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface, self)

        self.index_greetscreen = 0
        self.index_galleryscreen = 1
        self.index_picturescreen = 2

        if first_run:
            self.main_windows.setCurrentIndex(self.index_greetscreen)
        else:
            self.ftp = FTP()
            self.gallery_page()
        self.gallery_load()
        self.initUI()


    def initUI(self):
        self.button_save.clicked.connect(self.save_credentials)
        #TODO: to moke normal checkup
        if not first_run:
            self.button_upload.clicked.connect(self.ftp.upload_all)
        self.button_back.clicked.connect(self.gallery_page)

    def save_credentials(self):
        ip = self.input_server_ip.text()
        username = self.input_server_ip.text()
        password = self.input_server_ip.text()

        attempt = True  # self.ftp.connection_attempt(ip, username, password)

        if attempt:
            self.gallery_page()
        else:
            print('wrong')
        self.config_rewrite(ip=ip, username=username, password=password)
        self.ftp = FTP()

    def config_rewrite(self, ip, username, password):
        config.set('server', 'ip', ip)
        config.set('client', 'username', username)
        config.set('client', 'password', password)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def gallery_load(self):
        if gallery_dir:
            icons = [os.path.join(gallery_dir, picture)
                     for picture in os.listdir('gallery')]

            self.gridLayoutWidget = QWidget(self.page_gallery)
            self.gridLayoutWidget.setGeometry(QRect(30, 10, 320, 10))
            self.gridLayoutWidget.setObjectName("layout_gallery")
            self.layout_gallery = QGridLayout(self.scrolliing_area)
            self.layout_gallery.setSizeConstraint(QLayout.SetFixedSize)
            self.layout_gallery.setContentsMargins(14, 0, 0, 0)
            self.layout_gallery.setVerticalSpacing(6)

            row, column = 0, 0
            for index, image in enumerate(icons):
                button = QPushButton(self)
                button.clicked.connect(
                    lambda checked=None, x=image: self.picture_page(x))
                button.setMaximumSize(QSize(99, 127))
                button.setLayoutDirection(Qt.LeftToRight)
                button.setAutoFillBackground(False)
                button.setStyleSheet("background: #2A2A2A; border-radius: 0px")
                button.setText("")
                icon = QIcon()
                icon.addPixmap(QPixmap(image), QIcon.Normal, QIcon.Off)
                button.setIcon(icon)
                button.setIconSize(QSize(99, 127))
                button.setFlat(False)
                button.setObjectName("pic_" + str(index))
                self.layout_gallery.addWidget(button, row, column, 1, 1)

                column += 1
                if column == 3:
                    row += 1
                    column = 0

    def gallery_page(self):
        self.main_windows.setCurrentIndex(self.index_galleryscreen)

    def picture_page(self, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.image.setIcon(icon)
        self.button_download.clicked.connect(
            lambda checked=None, x=path: self.ftp.download(x))
        self.main_windows.setCurrentIndex(self.index_picturescreen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
