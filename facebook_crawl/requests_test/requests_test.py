__author__ = 'likang'
# -*- coding: utf-8 -*-
import urllib2, cookielib, re, os, sys,random

class Facebook():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        cj = cookielib.CookieJar()
        self.cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
       # proxy_http = ['http://182.239.95.134:80', 'http://113.105.224.86:80', 'http://183.207.229.196:80',
       #               'http://183.203.22.68:80', 'http://183.207.224.44:80', 'http://117.135.194.55:80',
       #               'http://183.203.22.96:80', 'http://182.239.127.137:80', 'http://183.207.228.60:80',
       #               'http://183.207.224.52:80']
        proxy_http = [ ]
        len_http = len(proxy_http)
        print len_http
        http_index = random.randint(0, len_http - 1)
        http_test = 8
        try:
            self.http_proxy_support = urllib2.ProxyHandler({"http": proxy_http[http_test]})
        except Exception, e:
            print '-----build proxy failed', e
        opener = urllib2.build_opener(self.http_proxy_support, self.cookie_support, urllib2.HTTPHandler)
        opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                            ('Content-Type', 'application/x-www-form-urlencoded'),
                            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
        self.opener = opener

    def login(self):
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        data = "locale=en_US&non_com_login=&email="+self.email+"&pass="+self.password+"&lsd=20TOl"

        usock = self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data)
        if "Logout" in usock.read():
            print "Logged in."
        else:
            print "failed login"
            print usock.read()
            sys.exit()

f.login()
