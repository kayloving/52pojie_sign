# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq
from .QYWX_Notify import WxNotify


cookie = ""
if not cookie:
    cookie = input("cookie")
QYWX_CORPID = ""
if not QYWX_CORPID:
    QYWX_CORPID = input("QYWX_CORPID")
QYWX_CORPSECRET = ""
if not QYWX_CORPSECRET:
    QYWX_CORPSECRET = input("QYWX_CORPSECRET")
QYWX_AGENTID = ""
if not QYWX_AGENTID:
    QYWX_AGENTID = input("QYWX_AGENTID")
QYWX_MEDIA_ID = ""
if not QYWX_MEDIA_ID:
    QYWX_MEDIA_ID = input("QYWX_MEDIA_ID")
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
wn = WxNotify(corpid=QYWX_CORPID, corpsecret=QYWX_CORPSECRET, agentid=QYWX_AGENTID, media_id=QYWX_MEDIA_ID)
wn.send('52破解签到信息', msg)
