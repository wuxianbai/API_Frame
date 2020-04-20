import unittest
from ddt import ddt, data, unpack

from util.testdata import TestData
from util.CheckResult import AssertResult
from util.HttpRequest import HttpRequest
import common.GlobalVars as gv
from BeautifulReport import BeautifulReport


values = TestData().getDatas()
correlationDict = {}

@ddt
class QrCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.req = HttpRequest()

    def tearDown(self):
        if self.tear_down is None:
            return
        tear_down_list = self.tear_down.split(';')
        for tdl in tear_down_list:
            param = tdl.split('=')
            values = self.result
            if param[1].count(']') == 1:
                gv.set_value(param[0], values[param[1][1:-1]])
            else:
                print(param[1].count(']'))
                for key in param[1][1:-1].split(']['):
                    try:
                        tmp = values[int(key)]
                        print(tmp)
                    except:
                        try:
                            tmp = values[key]
                            print(tmp)
                        except:
                            break
                    values = tmp
                gv.set_value(param[0], values)
        print(gv.get_values())

    @data(*values)
    @unpack
    def test_1(self, casename, url, method, params, expcet_data, tear_down):
        self._testMethodName = 'test_1_' + casename
        self._testMethodDoc = casename
        self.tear_down = tear_down
        correlationDict = gv.get_values()
        for key in correlationDict:
            if key in params:
                params = params.replace(key, correlationDict[key])
                # print(params)

        self.result = self.req.HttpRequests(method, url, params)
        res = AssertResult().is_equal(self.result, expcet_data)
        self.assertTrue(res)

if __name__ == '__main__':
    gv._init()
    # unittest.main()
    # suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.discover('./', '*.py')
    report = BeautifulReport(suite)
    """
                生成测试报告,并放在当前运行路径下
            :param report_dir: 生成report的文件存储路径
            :param filename: 生成文件的filename
            :param description: 生成文件的注释
            :param theme: 报告主题名 theme_default theme_cyan theme_candy theme_memories
            :return:
            """
    report.report(description='接口自动化', report_dir='../report/', filename='report.html')