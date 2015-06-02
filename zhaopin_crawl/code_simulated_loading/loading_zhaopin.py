# -*- coding: utf-8 -*-
'''
2015.03.11 18:28
Kang Li
'''
__author__ = 'likang'
import urllib2, cookielib,urllib
hosturl = 'http://i.zhaopin.com/Login/LoginManager/Login'
posturl = 'http://i.zhaopin.com/Login/LoginManager/Login'

class Zhaopin():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)
        urllib2.urlopen(hosturl)  
    def getopener(self):
        return self.opener
    def login(self):
        headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0',  
           'Referer' : 'http://i.zhaopin.com/Login/LoginManager/Login'}  
        postData = {
            'loginname' : self.email, 
            'password' : self.password, 
            'int_count' : '999',
            'errTimes' : '0',
            'bkurl': ''
            }  
        try:
            postData = urllib.urlencode(postData)
            try:
                request = urllib2.Request(posturl, postData, headers)
            except Exception, e:
                print '-----request failed', e
            try:   
                 response = urllib2.urlopen(request)  
                 text=response.read()
                 test_url = response.geturl()    
            except Exception, e:
                print '-----open failed', e
        except Exception, e:
            print '-----连接失败', e
            return 0
        if test_url !=None:
            flag = test_url.split('/')  # 分析登陆后得到的url，辨别是否登陆成功
            if len(flag)== 4:
                 print '-----log in succeed'
                 return 1  # 登陆成功返回1
            else:
                print '-----log in failed'
                return 0  # 登录失败返回0
def test():    
    f = Zhaopin("", "")
    f.login()
if __name__ == '__main__':
    test()
