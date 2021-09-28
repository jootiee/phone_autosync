from config import *


class FTP:
    def __init__(self):
        self.ftp = ftplib.FTP(ip, timeout=10)
        self.ftp.login(user=username, passwd=password)
        self.ftp.cwd(server_dir)
        self.ftp.encoding = "utf-8"
        self.ftp.cwd('/' + server_dir + '/')

    def upload_all(self):
        uploaded = False
        current_dir = os.listdir(gallery_dir)
        desired_dir = '/' + server_dir + '/'
        desired_dir_files = self.ftp.nlst()
        self.ftp.cwd('/' + server_dir + '/')
        if current_dir:
            for uploading in current_dir:
                if desired_dir + uploading in desired_dir_files:
                    continue
                send = os.path.join(gallery_dir, uploading)
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

    def download(self, pic):
        paths = get_paths(self.ftp)
        for index, path in enumerate(paths):
            if path in pic:
                selection = index
                break
        try:
            self.ftp.retrbinary(
                'RETR ' + paths[selection], open(os.path.join(gallery_dir, paths[selection]), 'wb').write)
            print('file downloaded')
        except:
            print("file is not on server")

    def connection_attempt(self, ip, username, password):
        try:
            ftp = ftplib.FTP(ip, timeout=10)
            ftp.login(user=username, passwd=password)
            return True
        except:
            return False