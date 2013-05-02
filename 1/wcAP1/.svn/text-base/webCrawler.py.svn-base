#!/usr/bin/env python
#coding:utf-8

from bae.core import const
import urllib, urllib2, cookielib
from django.http import HttpResponse
import os
import tempfile
from bae.api.memcache import BaeMemcache
import hashlib
import json
from utilities import *
import pickle



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
    #str+=crawler.testSend('TESTING')
    str+=crawler.sendWCMsg('这是一个测试', '1440591140');
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
        #cookies = self.loadCookie()
        cookies = cookielib.MozillaCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        resp = opener.open(BASE_WCURL+'/cgi-bin/login?lang=zh_CN',data)
        
        
        #parse response
        s=resp.read()
        #log(s)
        ret = json.loads(s)
        redir = ret['ErrMsg']
        token =matchStr(redir,'[\d]{8,}')
        #log('token='+token)
        cache.set('token',token)
        self.saveCookie(cookies)

        if(ret['Ret']==302):
            #login sucess
            cookies = self.loadCookie()
            
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
            resp = opener.open(BASE_WCURL+ret['ErrMsg'])
            rt = self.saveCookie(cookies)
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
        #pickle.dump(cookieJar, open(cookieFile,'w'))
        d = open(cookieFile,'r')
        ck = d.read()
        #ck = pickle.dumps(cookieJar,True)
        cache.delete('cookie')
        cache.set('cookie',ck)
        return ck
        
    def loadCookie(self):
        cache = BaeMemcache()
        cookie = cache.get('cookie')
        #cache.delete('cookie')
        #log(cookie)
        tempDIR = const.APP_TMPDIR
        cookieFile = tempDIR+'/cookies.txt'
        d = open(cookieFile,'w')
        d.write(cookie)
        d.close()
        cookies = cookielib.MozillaCookieJar(cookieFile)
        cookies.load(cookieFile,ignore_discard=True, ignore_expires=True)
        #cookies = pickle.loads(cookie)
#         cache.delete('cookie')
        return cookies
    
    def testSend(self,content):
        cache = BaeMemcache()
        token = cache.get('token')
        #log(token)
        fakeid = '1440591140'
        SENDER_DATA['tofakeid']=fakeid
        SENDER_DATA['token']=token
        SENDER_DATA['content']=content
        
        data = urllib.urlencode(SENDER_DATA)
        
        cookies = self.loadCookie()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        
        #opener.addheaders=[('Referer',BASE_WCURL+USERS_URL%(token,0))]
        #resp = opener.open(SENDER_REF%(token,fakeid))
        #rt = resp.read()
        
        #opener.addheaders=[('Referer',BASE_WCURL+SENDER_REF%(token,fakeid))]
        opener.addheaders=[('Referer',BASE_WCURL+INDEX_URL%token)]
        resp = opener.open(BASE_WCURL+SENDER_URL,data)
        #log(BASE_WCURL+SENDER_URL+data)
        rt=resp.read()
        self.saveCookie(cookies)       
        return rt
    
    def sendWCMsg(self,content,fakeId):
        """Send Message to user identified by the fakeid"""
        cache = BaeMemcache()
        token = cache.get('token')
        #log(token)

        SENDER_DATA['tofakeid']=fakeId
        SENDER_DATA['token']=token
        SENDER_DATA['content']=content
        
        data = urllib.urlencode(SENDER_DATA)
        
        cookies = self.loadCookie()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        opener.addheaders=[('Referer',BASE_WCURL+SENDER_REF%(token,fakeId))]
        resp = opener.open(BASE_WCURL+SENDER_URL,data)
        rt=resp.read()
        self.saveCookie(cookies)  
        ret = json.loads(rt)
        if(ret['ret']=='0'):
            return 'OK'
        else:
            return 'Failed.'
        