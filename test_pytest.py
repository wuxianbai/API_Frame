import requests

url = 'http://www.baidu.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'Content-Type': 'application/json'
    }
params = {
    'flag': 1,
    'task_set': "{'filter': 1}"
}

res = requests.get(url, params=eval(str(params)), headers=headers)
print(res.url)