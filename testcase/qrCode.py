import unittest
from ddt import ddt, data

from util.testdata import TestData
from util.CheckResult import CheckResult
from util.HttpRequest import HttpRequest
import common.GlobalVars as gv
from BeautifulReport import BeautifulReport
from util.MyLog import MyLog

MyLog().log('debug', '测试启动')
values = TestData().getDatas()
# correlationDict用来保存关联变量
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
                # print(param[1].count(']'))
                for key in param[1][1:-1].split(']['):
                    try:
                        tmp = values[int(key)]
                    except:
                        try:
                            tmp = values[key]
                        except:
                            break
                    values = tmp
                gv.set_value(param[0], values)

    @data(*values)
    # @unpack
    def test_1(self, *args):
        ID, casename, url, method, params, expcet_data, tear_down = args[0]
        MyLog().log('debug', '用例{}-{}开始执行测试'.format(ID, casename))
        # 主要是为了报表展示，显示指定的用来描述和方法名称
        self._testMethodName = 'test_1_' + casename
        self._testMethodDoc = casename
        self.tear_down = tear_down
        correlationDict = gv.get_values()
        for key in correlationDict:
            if key in params:
                params = params.replace(key, correlationDict[key])

        self.result = self.req.HttpRequests(method, url, params)
        if not self.result:
            res = False
        else:
            res = CheckResult().is_equal(self.result, expcet_data)
        self.assertTrue(res)


if __name__ == '__main__':
    gv._init()
    suite = unittest.defaultTestLoader.discover('./', 'qrCode.py')
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
