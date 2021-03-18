# 52pojie_sign

## 只支持一个帐号签到
### 每天北京时间早上8:01签到
如要更改签到时间，在.github/workflows/52pojie.yml中修改cron表达式。
如本签到系统的cron表达式为 '1 0 * * * *'，代表标准时间00：01， 第一位是分，第二位是时，后面三位为**，表示不做限制。北京时间属于东八区，时位+8，既是北京时间早上8:01

### 在setting-secrets里新建两个secret
1. secret名 COOKIE
   secret值 你的52pojie cookie
2. secret名 SCKEY
   secret值 你的sckey
   
   
### 获取52pojie cookie
1. 手动登录52pojie网站
2. 按下F12或右键检查打开开发者工具，点击网络(network)选项卡
3. 刷新网页，拉动开发者工具界面滑动条到顶部，找到52pojie.cn并点击
4. 开发者工具右侧点击标头(headers)，下拉滑动条，找到请求标头（request headers），复制cookie中的 #### htVD_2132_saltkey=xxxxx;htVD_2132_auth=xxxxxx'两项

### 由于server酱旧版通知即将下线，新版通知次数有限，企业微信群机器人通知无法在普通微信端查看，因此用企业微信应用通知替代server酱，可直接在微信端接收通知
1.新建QYWX_CORPID,QYWX_CORPSECRET,QYWX_AGENTID,QYWX_MEDIA_IA 4个secrets
2.分别填入企业ID，secret，agentID，media_id（media_id可填入0，发送文字卡片通知）
3.[参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note) [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note)

~~### 使用企业微信群机器人通知，替代server酱
复制企业微信群机器人的webhook:https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx
复制key=后面的字符串
创建secret QYWX_KEY
值填入上面复制的字符串~~
    
 
 
 
 
