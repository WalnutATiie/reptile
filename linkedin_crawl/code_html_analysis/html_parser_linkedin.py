#!/usr/bin/python 
# -*- coding: utf-8 -*-

'''
Created on 2015-3-31
@author: Kang Li
@name: login_linkedin.py
'''
import json
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Person():
    '''
    Target fields that we wish to scrap
    '''
    def __init__(self , res):
        self.name = None  # 姓名
        self.location = None  # 所在地
        self.industry = None  # 领域
        self.industryEng = None  # 领域英文名
        self.website = None  # 个人主页
        self.address = None  # 地址
        self.public_profile_url = None  # 公开的个人档案url
        self.companies = []  # 工作过的公司
        self.educations = []  # 学习经历
        self.skills = []  # 技能
        self.hobbies = []  # 爱好
        self.member_connections = None  # 好友数
        self.imgurl = None  # 个人照片url
        self.email = None  # 邮箱
        self.im = None  # 即时通讯
        self.twitter = None  # twitter
        self.phone_numbers = None  # 电话号码
        self.res = res  # 用户简历界面html代码内容
        self.connections_url = []
    def parse_basic(self):
        '''
        Scrap basic details for person
        '''       
        soup = BeautifulSoup(self.res)
        self.name = soup.find("span", "full-name").text
        print "fetching " + self.name +"'s basic information…"
        self.industry = soup.find("dd", "industry")
        if self.industry != None:
            self.industry = soup.find("dd", "industry").contents[0].text
        self.industryEng = soup.find("div", id="headline").contents[0].text
        self.imgurl = soup.find("div", "profile-picture")
        if self.imgurl != None:
            self.imgurl = soup.find("div", "profile-picture").find("img").get("src")
        self.location = soup.find("a", attrs={"name": "location"}).text
        companies = soup.find_all("a", attrs={"name": "company"})
        if companies != None :
            for single_company in companies:
                self.companies.append(single_company.text)
            self.companies = self.companies[0:len(self.companies) / 2]  # 因为在相同的公司的结果重复一遍 所以截取list删除重复的
        educations = soup.find_all("a", attrs={"title": "学校详细信息"})
        if educations != None:
            for single_education in educations:
                self.educations.append(single_education.text)
            self.educations = self.educations[1:len(self.educations)]  # 去掉第一个重复的教育经历
        self.email = soup.find("div", id="email").text
        self.im = soup.find("div", id="im").text
        self.phone_numbers = soup.find("div", id="phone").text
        self.address = soup.find("div", id="address").text
        self.twitter = soup.find("div", id="twitter").text
        self.website = soup.find("div", id="website").text
        self.public_profile_url = soup.find("a", "view-public-profile").text
        skills = soup.find_all("span", "endorse-item-name-text")
        if skills != None:
            for single_skill in skills:
                self.skills.append(single_skill.text)
        hobbies = soup.find("div", id="interests-view")
        if hobbies != None:
            self.hobbies = hobbies.text.split(',')
        self.member_connections = soup.find("a", "connections-link").text
        connections_urls = soup.find_all("a", "connections-name")
        if connections_urls != None:
            for single_url in connections_urls:
                self.connections_url.append(single_url.get("href"))
    def saveProfilePage(self):  # 保存http页面
         print "saving " + self.name +"'s profile page…"
         file_object = open('out_profile_html_page/' + self. name + '.html', 'w')
         file_object.write(self.res)
         file_object.close()
    def SaveAsJson(self):
        print "saving " + self.name +"'s information as json…"
        dict = {'name':self.name, 'location':self.location, 'industry':self.industry, 'industryEng':self.industryEng, 'website':self.website, 'address':self.address,
              'public_profile_url':self.public_profile_url, 'companies':self.companies, 'educations':self.educations,
              'skills':self.skills, 'hobbies':self.hobbies, 'member_connections':self.member_connections, 'imgurl':self.imgurl,
              'email':self.email,'im':self.im,'twitter':self.twitter,'phone_numbers':self.phone_numbers,
              'connections_url':self.connections_url
              }
        out_jscon = json.dumps(dict, ensure_ascii=False, encoding="utf-8").encode("utf-8")
        file_jscon = open('out_personal_json/' + self.name + '.json', 'w')
        file_jscon.write(out_jscon)
        file_jscon.close()
    def get_connections_url(self):
        return self.connections_url
def test():    
    file_object = open('123.html', 'r') 
    res = file_object.read()
    file_object.close()
    person_information = Person(res)
    person_information.parse_basic()
    person_information.print_basic()
if __name__ == '__main__':
    test()
