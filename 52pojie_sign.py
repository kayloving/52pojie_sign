# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq
from QYWX_Notify import WxNotify
import os


cookie = os.getenv("cookie")
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
headers = {'cookie': cookie,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
requests.get(url1, headers=headers)
req = requests.get(url, headers=headers).text
doc = pq(req)
msg = doc('.vwmy a').text() + '\t' + doc('#messagetext p').text()
print(msg)
if not cookie:
    print('cookie为空')
QYWX_CORPID = os.getenv("QYWX_CORPID")
QYWX_CORPSECRET = os.getenv("QYWX_CORPSECRET")
QYWX_AGENTID = os.getenv("QYWX_AGENTID")
QYWX_MEDIA_ID = os.getenv("QYWX_MEDIA_ID")
wn = WxNotify(corpid=QYWX_CORPID, corpsecret=QYWX_CORPSECRET, agentid=QYWX_AGENTID, media_id=QYWX_MEDIA_ID)
wn.send('52破解签到信息', msg)
