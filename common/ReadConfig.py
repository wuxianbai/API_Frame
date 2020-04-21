from configparser import ConfigParser

class ReadConfig():
    def __init__(self, filename=None):
        if filename is None:
            self.filename = './config/qrCode.ini'

    def read(self):
        self.cp = ConfigParser()
        self.cp.read(filenames=self.filename)

    def get(self, session, option):
        self.read()
        return self.cp.get(session, option)

if __name__ == '__main__':
    rc = ReadConfig()
    rc.read()
    r = rc.get('qrCode', 'ID')
    print(r)