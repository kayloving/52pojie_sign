# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq
import json


class WxNotify:
    def __init__(self, corpid, corpsecret, agentid,media_id):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid
        self.media_id = media_id
        self.access_token = self.__get_access_token(corpid, corpsecret)

    def __get_access_token(self, corpid, corpsecret):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        resp_json = resp.json()
        if 'access_token' in resp_json.keys():
            return resp_json['access_token']
        else:
            raise Exception('Please check if corpid and corpsecret are correct \n' + resp.text)

    def send(self, title, text):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.access_token
        data = {
            "touser": "@all",
            "msgtype": "mpnews",
            "agentid": self.agentid,
            "mpnews": {
                "articles": [
                    {
                        "title": title,
                        "thumb_media_id":self.media_id,
                        "author": "",
                        "content_source_url": "",
                        "content": text,
                        "digest": text
                    }
                ]
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        resp = requests.post(url, data=json.dumps(data))
        resp.raise_for_status()
        return resp.json()
    

cookie=""
if not cookie:
    cookie = input("输入cookie")
QYWX_AM = ""
if not QYWX_AM:
    QYWX_AM = input("输入QYWX_AM")
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
headers = {'cookie':cookie,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
requests.get(url1, headers=headers)
req = requests.get(url, headers=headers).text    
doc = pq(req)
msg = doc('.vwmy a').text() + '\t' + doc('#messagetext p').text()
print(msg)
print(QYWX_AM)
# if not cookie:
#     print('cookie为空')
# corpid,corpsecret,agentid,media_id = QYWX_AM
# wn = WxNotify(corpid=corpid, corpsecret=corpsecret, agentid=agentid,media_id=media_id)
# wn.send('52破解签到信息', msg)


