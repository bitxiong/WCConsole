import urllib, urllib2, cookielib
import json
#bae.core.const.APP_TMPDIR
import hashlib
from utilities import *
import re

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

m = hashlib.md5('142536')
crpt = m.hexdigest()
info ={'username':'alexxiong.it.cupsa@gmail.com','pwd':crpt,
       'imgcode':'','f':'json'}

data = urllib.urlencode(info)
print BASE_WCURL+'/cgi-bin/login?lang=zh_CN'

resp = opener.open(BASE_WCURL+'/cgi-bin/login?lang=zh_CN',data)

print resp.read()
add = '/cgi-bin/indexpage?t=wxm-index&lang=zh_CN&token=509109889'

#resp = opener.open(BASE_WCURL+add)
p = 'http://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
str = ''
SENDER_DATA['tofakeid']='1440591140'
SENDER_DATA['token']='509109889'
SENDER_DATA['content']='YOYO'

datas= urllib.urlencode(SENDER_DATA)

request = urllib2.Request(p,datas)

request.add_header('Referer','http://mp.weixin.qq.com/cgi-bin/singlemsgpage?token=509109889&fromfakeid=1440591140&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN')
resp = opener.open(request)
print datas
print resp.read()