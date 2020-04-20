from common.ReadExcel import ReadExcel
from util.GetData import GetData
from util.MyLog import MyLog


class TestData():

    @classmethod
    def getDatas(cls):
        MyLog().log('debug', '开始获取excel测试用例')
        gd = GetData()
        readExcel = ReadExcel()

        nrows = readExcel.get_rows()
        values = []
        session = 'qrCode'
        for row in range(1, nrows):
            dic = []
            # 因为excel表格格式是固定的，所以在获取数据的时候将参数固定，如果后面有调整的时候再做一定的修改
            dic.append(int(gd.getValue(row, session, 'ID')))
            dic.append(gd.getValue(row, session, 'case_name'))
            dic.append(gd.getValue(row, session, 'url'))
            dic.append(gd.getValue(row, session, 'method'))
            dic.append(gd.getValue(row, session, 'params'))
            dic.append(gd.getValue(row, session, 'expcet_data'))
            dic.append(gd.getValue(row, session, 'tear_down'))
            values.append(dic)

        return values


if __name__ == '__main__':
    value = TestData().getData()
    print(value)
