import unittest
from BeautifulReport import BeautifulReport
import common.GlobalVars as gv

if __name__ == '__main__':
    gv._init()
    suite = unittest.defaultTestLoader.discover('./testcase/', 'qrCode.py')
    report = BeautifulReport(suite)
    report.report(description='接口自动化', report_dir='./report/', filename='report.html')