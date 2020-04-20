from common.ReadExcel import ReadExcel
from common.UserVars import UserVars
import re


class GetData():
    def __init__(self):
        self.readExcel = ReadExcel()

    def getValue(self, row, session, option):
        data = self.readExcel.get_cell_value(row, session, option)
        if data == '':
            return None

        # 替换请求参数中的变量
        if option == 'params':
            data = self.replaceVars(data)
        return data

    def replaceVars(self, params):
        # 获取params中的所有变量，'\${.*?}'加?是非贪婪模式，可以匹配所有的变量
        vars = re.findall('\${.*?}', params)
        for var in vars:
            # 有的变量属于方法，会有参数(一个或多个)，有的没有参数，此处用来针对参数不同情况分别做处理
            if '(' not in var:
                var_tmp = var[2:-1]
            else:
                index = var.index('(')
                args = eval(var[index:-1])
                var_tmp = var[2:index]

            func = getattr(UserVars(), var_tmp, None)
            # 如果只有一个参数，处理后会是一个整数，如果多个参数，处理后会是一个元组
            if func is not None:
                if isinstance(args, int):
                    tmp = func(args)
                else:
                    tmp = func(*args)
                params = params.replace(var, tmp)
        return params

if __name__ == '__main__':
    gd = GetData()
    params = '''
    {'puid': 35, 'requestType': 'coverSweepGoldenReceiver', 'sendtype': 'C2B消费', 'sendData':'[{"fid":532,"keyword":"acqCode","value":"48020000"},{"fid":533,"keyword":"merId","value":"777290058135880"},{"fid":534,"keyword":"merCatCode","value":"5811"},{"fid":535,"keyword":"merName","value":"商户名称"},{"fid":537,"keyword":"txnAmt","value":"30000"},{"fid":538,"keyword":"termId","value":"49000002"},{"fid":539,"keyword":"qrNo","value": "${qrNo}"},{"fid":540,"keyword":"backUrl","value":"http://101.231.204.84:8091/sim/notify_url2.jsp"},{"fid":541,"keyword":"orderNo","value": "${createRandomNums(14, 1)}"},{"fid":542,"keyword":"orderTime","value":"20200414145953"}]'}
    '''
    gd.replaceVars(params)
    # url = gd.getExpectData(2, 'qrCode')
    # print(url)