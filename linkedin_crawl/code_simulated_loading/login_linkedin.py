#!/usr/bin/python 
# -*- coding: utf-8 -*-

'''
Created on 2015-3-27
@author: Kang Li
@name: login_linkedin.py
'''
import requests
from bs4 import BeautifulSoup
class Linkedin():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.client = requests.Session()
    def login(self):   
        

        HOMEPAGE_URL = 'https://www.linkedin.com'
        LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

        html = self.client.get(HOMEPAGE_URL).content
        soup = BeautifulSoup(html)
        csrf = soup.find(id="loginCsrfParam-login")['value']

        login_information = {
                             'session_key':self.email,#账号
                             'session_password':self.password,#密码
                             'loginCsrfParam': csrf,
                             }

        self.client.post(LOGIN_URL, data=login_information)
        #res=self.client.get('http://www.linkedin.com/profile/preview?locale=zh_CN&trk=prof-0-sb-preview-primary-button')#profile预览界面
        res=self.client.get('http://www.linkedin.com/profile/preview?locale=zh_CN&trk=prof-0-sb-preview-primary-button')
        home_soup = BeautifulSoup(res.text)
        if "Sign In" in home_soup.title.string:#登陆失败 返回的html标题为Sign In
            print "Failed to log in... :'("
            return 0  # 登录失败返回0
        else :
            print "Log-in success!"
            file_object = open('123.html', 'w') 
            file_object.write(res.content)
            file_object.close()
            return 1  # 登陆成功返回1
    def get_client(self):
        return self.client
def test():    
    f = Linkedin("", "")
    f.login()
if __name__ == '__main__':
    test()
#client.get('Any_Linkedin_URL')
