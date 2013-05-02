#coding:UTF-8
from wcData import *
from utilities import *
import urllib, urllib2, cookielib
import weibo

class wcMsgProccessor:
    def parseMsg(self,wcMsg, WCUser):
        
        #------------------processing---------------------------
        if (wcMsg.msgType == MESSAGE_TEXT):
            response = wcTextResponse()
            response.resContent = wcMsg.msgContent
            log(wcMsg.msgHost)
  
            #msg is from onkeylive
            if(wcMsg.msgHost == WC_HOSTS['onkeylive']):
                resp = self.sendToWeibo(wcMsg.msgContent)
                log(resp)
                response.resContent = resp
                
            #msg is from gossip_cuhk
            elif (wcMsg.msgHost == WC_HOSTS['gossip_cuhk']):
                resp = self.sendToWeibo(wcMsg.msgContent)
                log(resp)
                response.resContent = resp
                
            #msg is from the CUPSA official platform
            elif (wcMsg.msgHost == WC_HOSTS['cupsa']):
                response.resContent = 'This the official public platform of CUPSA. You inquiry is well received. Thanks.'
        
        
        
        #------------------------------------------------------
        return response #a string containing return string
    
    def sendToWeibo(self,msg):
        
        client=weibo.APIClient(WEIBO_APPKEY,
                       WEIBO_APPSEC, 
                       # modify it.
                       WEIBO_USER,
                       WEIBO_PASS)
        try:
            r=client.post.statuses__update(source=WEIBO_APPKEY,
                               status=msg)
            return '发出去啦！'
        except:
            return '发送失败！'
        