from bae.core import const
import urllib, urllib2, cookielib
from django.http import HttpResponse
import os
import tempfile
from bae.api.memcache import BaeMemcache
import hashlib
import json
from utilities import *


def testWeb(request):
    cache = BaeMemcache()
    craw = webCrawler()
    cookies = craw.loadCookie()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
    
    m = hashlib.md5('142536')
    crpt = m.hexdigest()
    info ={'username':'alexxiong.it.cupsa@gmail.com','pwd':crpt,
       'imgcode':'','f':'json'}
    data = urllib.urlencode(info)
    
    resp = opener.open(BASE_WCURL+'/cgi-bin/login?lang=zh_CN',data)
    craw.saveCookie(cookies)
    
    s=resp.read()
    ret = json.loads(s)
    cache.set('token',ret['ErrMsg'])
    return HttpResponse(ret['ErrMsg'])

def testCrawler(request):
    crawler = webCrawler()
    str=crawler.plainLogin('alexxiong.it.cupsa@gmail.com','142536')
    str+=crawler.testSend('TESTING')
    return HttpResponse(str)

class webCrawler:
    def plainLogin(self,user,pwd):
        cache = BaeMemcache()
        m = hashlib.md5(pwd)
        crpt = m.hexdigest()
        info ={'username':user,'pwd':crpt,
       'imgcode':'','f':'json'}
        data = urllib.urlencode(info)
        
        #HTTP Fetch
        cookies = self.loadCookie()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        resp = opener.open(BASE_WCURL+'/cgi-bin/login?lang=zh_CN',data)
        self.saveCookie(cookies)
        
        #parse response
        s=resp.read()
        log(s)
        ret = json.loads(s)
        redir = ret['ErrMsg']
        token =matchStr(redir,'[\d]{8,}')
        #log('token='+token)
        cache.set('token',token)
        if(ret['Ret']==302):
            #login sucess
            resp = opener.open(BASE_WCURL+(INDEX_URL%cache.get('token')))
            self.saveCookie(cookies)
            return 'Login Success! '
        else:
            #login failed
            #To-do: Add a verification code handling routine
            
            #end to-do
            self.saveCookie(cookies)
            
            return 'Login Failed! '
        
    def saveCookie(self,cookieJar):
        cache = BaeMemcache()
        tempDIR = const.APP_TMPDIR
        cookieFile = tempDIR+'/cookie.txt'
        cookieJar.save(cookieFile,ignore_discard=True, ignore_expires=True)
        d = open(cookieFile,'r')
        cache.set('cookie',d.read())
        
    def loadCookie(self):
        cache = BaeMemcache()
        cookie = cache.get('cookie')
        tempDIR = const.APP_TMPDIR
        cookieFile = tempDIR+'/cookie.txt'
        d = open(cookieFile,'w')
        d.write(cookie)
        d.close()
        cookies = cookielib.MozillaCookieJar(cookieFile)
        cookies.load(cookieFile)
        return cookies
    
    def testSend(self,content):
        cache = BaeMemcache()
        token = cache.get('token')
        #log(token)
        SENDER_DATA['tofakeid']='1440591140'
        SENDER_DATA['token']=token
        SENDER_DATA['content']=content
        
        data = urllib.urlencode(SENDER_DATA)
        
        cookies = self.loadCookie()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        resp = opener.open(BASE_WCURL+SENDER_URL,data)
        log(BASE_WCURL+SENDER_URL+data)
        self.saveCookie(cookies)       
        return resp.read()
        