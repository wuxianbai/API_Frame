import unittest, os
from BeautifulReport import BeautifulReport
import common.GlobalVars as gv
import util.SendEmail as se

if __name__ == '__main__':
    gv._init()
    suite = unittest.defaultTestLoader.discover('./testcase/', 'qrCode.py')
    report = BeautifulReport(suite)
    report.report(description='接口自动化', report_dir='./report/', filename='report.html')

    sender = '454762930@qq.com'
    pwd = 'iyayyxtpocqjcacb'
    receiver = '454762930@qq.com'
    smtpserver = 'smtp.qq.com'
    port = 465
    report = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'report', 'report.html')
    se.send_email(sender, pwd, receiver, smtpserver, port, report)