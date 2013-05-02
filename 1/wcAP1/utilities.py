import os
import sys
import re

def log(str):
    if 'SERVER_SOFTWARE' in os.environ:
        from bae.api import logging
        logging.info(str)
    else:
        print str
        
MESSAGE_TEXT = 1
MESSAGE_IMG =2
MESSAGE_SOUND =3
MESSAGE_NULL =0

RESPONSE_NULL=0
RESPONSE_TEXT=1

API_KEY = 'aOTrpGf8Zgyn4GvFYfMYG1lV'
API_SEC = 'o6Af5GMrQU7sTQC7sMC2NL4iKWyzT4oF'

BASE_WCURL = 'https://mp.weixin.qq.com'
INDEX_URL = '/cgi-bin/indexpage?t=wxm-index&lang=zh_CN&token=%s'
MSGLIST_URL = '/cgi-bin/getmessage?t=wxm-message&token=%s&lang=zh_CN&count=%d'
USERS_URL = '/cgi-bin/contactmanagepage?t=wxm-friend&token=%s&lang=zh_CN&pagesize=10&pageidx=0&type=0&groupid=%d'
SENDER_URL = '/cgi-bin/singlesend?t=ajax-response&lang=zh_CN&'
SENDER_REF = '/cgi-bin/singlemsgpage?token=%s&fromfakeid=%s&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'
SENDER_DATA = {'ajax':'1','content':'','error':'false','tofakeid':'','token':'','type':'1',}

WEIBO_APPKEY = '742769856'
WEIBO_APPSEC = '11815b85337e68a760132282f153a3aa'
WEIBO_USER = 'alexxiong.it.cupsa@gmail.com'
WEIBO_PASS = '142536'

WC_HOSTS = {'onkeylive':'gh_458b49493683','gossip_cuhk':'gh_87cdb4881e34','qnaxiong':'','cupsa':'gh_559169ff10ae',}

def matchStr(input,regexp):
    match = re.search(regexp, input)
    if match:
        return match.group(0)
    else:
        return ''
    
TRANSLATE_API = 'http://openapi.baidu.com/public/2.0/bmt/translate'
TRANS_FROM = 'auto'
TRANS_TO = 'auto'