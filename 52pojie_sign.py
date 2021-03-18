# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq
import json
import os
from QYWX_Notify import WxNotify

cookie = os.getenv("COOKIE").strip()
corpid = os.getenv("QYWX_CORPID").strip()
corpsecret = os.getenv("QYWX_CORPSECRET").strip()
agentid = os.getenv("QYWX_AGENTID").strip()
media_id = os.getenv("QYWX_MEDIA_ID").strip()
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
url2 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
headers = {'cookie': cookie,
           "ContentType": "text/html;charset=gbk",
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
requests.get(url1, headers=headers)
req = requests.get(url2, headers=headers).text
doc = pq(req)
un = doc('.vwmy a').text()
msg = doc('#messagetext p').text()
if '不是进行中的任务' in msg:
    msg = '今日已签到'
elif '恭喜' in msg:
    msg = '签到成功'
else:
    msg = '签到失败，请检查cookie或稍后重试'
msg = un + '\n' + msg
wx = WxNotify(corpid, corpsecret, agentid, media_id)
wx.send('52破解签到信息', msg)
