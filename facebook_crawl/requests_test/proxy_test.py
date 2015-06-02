# -*- coding: utf-8 -*-
import requesocks as requests
#import socks
#import socket
session = requests.session()
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
#socket.socket = socks.socksocket
session.proxies = {'http': 'socks5://127.0.0.1:9150',
                   'https': 'socks5://127.0.0.1:9150'}
#resp = session.get('https://www.facebook.com/login.php?login_attempt=1')
resp = session.get('https://www.facebook.com')
print resp.text
#import urllib2
#print urllib2.urlopen('http://www.baidu.com').read()