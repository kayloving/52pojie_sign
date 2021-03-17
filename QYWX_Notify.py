import requests
import json

class WxNotify:
    def __init__(self, corpid, corpsecret, agentid, media_id='0'):
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
            "agentid": self.agentid,
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        if self.media_id != '0':
            data["msgtype"] = 'mpnews'
            data["mpnews"] = {
                "articles": [
                    {
                        "title": title,
                        "thumb_media_id": self.media_id,
                        "author": "",
                        "content_source_url": "",
                        "content": text,
                        "digest": text
                    }
                ]
            }
        else:
            data["msgtype"] = "textcard"
            data["textcard"] = {
                "title": title,
                "description": text,
                "url": "URL"}
        resp = requests.post(url, data=json.dumps(data))
        resp.raise_for_status()
        return resp.json()
