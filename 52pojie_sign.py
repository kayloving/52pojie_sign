# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq
import json


cookie = ""
if not cookie:
    cookie = input('cookie')
qywx_key = ""
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
headers = {'cookie': cookie,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
requests.get(url1, headers=headers)
req = requests.get(url, headers=headers).text
doc = pq(req)
msg = doc('.vwmy a').text() + '\t' + doc('#messagetext p').text()
msg = '52破解签到信息' + '\n' + msg
print(msg)
requests.post(
        url=f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qywx_key}",
        data=json.dumps({"msgtype": "text", "text": {"content": msg}}),
    )

