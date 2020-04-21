import requests, json, re

from util import ToJson
from util.MyLog import MyLog

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Content-Type': 'application/json'
}


class HttpRequest():

    def HttpGet(self, url, data, header=None):
        if header is not None:
            response = requests.get(url, params=eval(data), headers=headers)
        else:
            response = requests.get(url, params=eval(data))

        if response.status_code != 200:
            MyLog().log('error', '请求失败，响应码为{}'.format(response.status_code))
            return False
        res = json.dumps(response.text, ensure_ascii=False)

        if not isinstance(res, dict):
            res = ToJson.qrCodeToJson(res)
        return res

    def HttpPost(self, url, data, header=None):
        if header is not None:
            response = requests.get(url, data=data, headers=headers).text
        else:
            response = requests.get(url, data=data).text
        res = json.dumps(response, ensure_ascii=False)
        return res

    def HttpRequests(self, method, url, data, header=None):
        MyLog().log('debug', '发送http-{}请求'.format(method))

        if method.lower() == 'get':
            result = self.HttpGet(url, data, header)
        elif method.lower() == 'post':
            result = self.HttpPost(url, data, header)
        MyLog().log('debug', 'http请求完成'.format(method))
        return result


if __name__ == '__main__':
    # pass
    hr = HttpRequest()
    url = 'https://open.unionpay.com/ajweb/help/qrcodeFormPage/sendOk'
    data = {'puid': 34, 'requestType': 'coverSweepReceiverApp', 'sendtype': 'C2B码申请',
            'sendData': '[{"fid":523,"keyword":"issCode","value":"90880019"},{"fid":525,"keyword":"backUrl","value":"http://101.231.204.84:8091/sim/notify_url2.jsp"},{"fid":526,"keyword":"qrType","value":""},{"fid":527,"keyword":"reqAddnData","value":""},{"fid":646,"keyword":"emvCodeIn","value":""},{"fid":528,"keyword":"accNo","value":"5216261000000002485"},{"fid":529,"keyword":"name","value":"宋小"}]'}

    res = hr.HttpRequests('get', url, data)
    # print(HttpRequest.AssertResponse('a', 1))
