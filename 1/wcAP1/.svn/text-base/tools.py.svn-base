from utilities import *
import urllib, urllib2, cookielib
import json

class Translator():
    def trans(self,content):
        TransData = {'from':TRANS_FROM,'to':TRANS_TO,'client_id':API_KEY,'q':content,}
        data = urllib.urlencode(TransData)
        
        resp = urllib2.urlopen(TRANSLATE_API, data)
        
        ret = json.loads(resp.read())
        
        tr_rst = ret['trans_result'][0]
        
        rt_str = 'Translating:"%s" to "%s" '%(tr_rst['src'],tr_rst['dst'])
        
        return rt_str
    
t = Translator()
print t.trans('Just Testing.')
        