from config import *


class FTP:
    def __init__(self):
        self.ftp = ftplib.FTP(ip, timeout=10)
        self.ftp.login(user=username, passwd=password)
        self.ftp.cwd(server_dir)
        self.ftp.encoding = "utf-8"
        self.ftp.cwd('/' + server_dir + '/')

    def upload(self):
        uploaded = False
        current_dir = os.listdir(upload_dir)
        desired_dir = '/' + server_dir + '/'
        desired_dir_files = self.ftp.nlst()
        self.ftp.cwd('/' + server_dir + '/')
        if current_dir:
            for uploading in current_dir:
                if desired_dir + uploading in desired_dir_files:
                    continue
                send = os.path.join(upload_dir, uploading)
                try:
                    self.ftp.storbinary(f'STOR {uploading}', open(send, 'rb'))
                    uploaded = True
                    compress(send)
                    print('success')
                except ftplib.error_perm as codes:
                    error_code = str(codes).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], "you don't have permission to upload here")
                        uploaded = False
            if not uploaded:
                print('all files are already on server')
        else:
            print('gallery is clear')

    def download(self):
        paths = current_dir_contains(self.ftp)

        [print(index, elem) for index, elem in enumerate(paths)]

        selection = 1

        try:
            self.ftp.retrbinary(
                'RETR ' + paths[selection], open(paths[selection], 'wb').write)
            print('file downloaded')
        except ftplib.error_perm as codes:
            error_code = str(codes).split(None, 1)
            if error_code[0] == '550':
                print(
                    error_code[1], "file may not exist or you may not have permission to view it")

    def connection_attempt(ip, username, password):
        try:
            ftp = ftplib.FTP(ip, timeout=10)
            ftp.login(user=username, passwd=password)
            return True
        except ftplib.all_errors as e:
            return False

    def run(self):
        while True:
            print('what do you want to do? \n 0 - upload; 1 - download')
            choice = int(input())

            if not choice:
                self.upload()
            elif choice == 1:
                self.download()
