import requests, json, urllib.parse

# url = 'https://open.unionpay.com/tjweb/tool/qrcodeFormPage/coverSweepReceiverApp'
url = 'https://open.unionpay.com/ajweb/help/qrcodeFormPage/sendOk'

data = {
    'puid': 34,
    'requestType': 'coverSweepReceiverApp',
    'sendtype': 'C2B码申请',
    'sendData': '[{"fid":523,"keyword":"issCode","value":"90880019"},{"fid":525,"keyword":"backUrl","value":"http://101.231.204.84:8091/sim/notify_url2.jsp"},{"fid":526,"keyword":"qrType","value":""},{"fid":527,"keyword":"reqAddnData","value":""},{"fid":646,"keyword":"emvCodeIn","value":""},{"fid":528,"keyword":"accNo","value":"6216261000000002485"},{"fid":529,"keyword":"name","value":"宋小"}]'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Content-Type': 'application/json'
}

res = requests.get(url, params=data, headers=headers)
# res = requests.get(url)
print(res.url)
print('----'*5)
print(res.text)