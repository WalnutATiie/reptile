# -*- coding: utf-8 -*-
'''
2015.03.11 18:28
Kang Li
'''
import urllib2, re,json
from bs4 import BeautifulSoup
def UTF2Hex(s):
    temp = s.encode("UTF-8").encode("hex")
    line = ""
    for i in range(0,len(temp)-1,2):
        line += "\\x" + temp[i] + temp[i+1]
    return line
class UserInfo():#用户信息类
    def __init__(self , opener):
        self.name = None#姓名
        self.sex = None#性别
        self.birthday=None#出生日期
        self.marriage=None
        self.hukou= None
        self.livingplace=None
        self.profile=None
        self.cerficationName=None
        self.cerficationNumber=None
        self.phone=None
        self.email=None
        self.image= None#照片
        self. resume_preview_url=None
        self.opener = opener
    def saveResumePage(self):#保存http页面
        req_resume_preview=urllib2.Request(self.resume_preview_url)
        resume_preview_content=self.opener.open(req_resume_preview)
        resume_preview_message=resume_preview_content.read()#简历预览页面的html
        file_object = open('out_resume_html_page/' + self. name+ '.html', 'w') #self.saveHttpPage(resume_preview_message)#保存简历页面，所有的详细个人资料都在里面
        file_object.write(resume_preview_message)
        file_object.close()
    def getUserInfo(self):#获取用户个人信息
        personal_url='http://i.zhaopin.com/'#登陆成功之后的主页
        req_personal=urllib2.Request(personal_url)
        content = self.opener.open(req_personal)
        message = content.read() 
        soup=BeautifulSoup(message)
        self_url = soup.find(id="mpi_a").get('href')#解析网页，定位到个人信息页面的url
        req_self=urllib2.Request(self_url)#个人信息页面url
        content = self.opener.open(req_self)
        self_message = content.read()#访问页面
        soup=BeautifulSoup(self_message)#解析个人信息
        self.name=soup.find(id="username").get('value')#姓名
        self.birthday=soup.find(id="birth_date_y").get('value')+'.' +soup.find(id="birth_date_m").get('value')#出生年月
        self.phone=soup.find(id="contact_num0").get('value')#联系电话
        self.email=soup.find(id="emailshow").get("value")#邮箱
        self.cerficationNumber=soup.find(id="id_number").get('value')#证件号
        #其他信息由于在当前页面是动态生成的，故改调用其他页面
        data_url='http://my.zhaopin.com/myzhaopin/resume_list.asp'#通过简历url获取用户个人信息，因为其html格式简单
        req_resume = urllib2.Request(data_url)
        content = self.opener.open(req_resume)
        message = content.read() 
        resume_id=re.search(r'\bresume_id\b.*\b"',message)#在html中获取resume_id
        resume_id=resume_id.group(0).split('"')
        resume_id=resume_id[1]#得到第一个resume_id
        resume_preview_url='http://my.zhaopin.com/MYZHAOPIN/resume_preview.asp?'+resume_id#简历预览页面的url
        self.resume_preview_url=resume_preview_url#保存简历页面的url
        req_resume_preview=urllib2.Request(resume_preview_url)
        resume_preview_content=self.opener.open(req_resume_preview)
        resume_preview_message=resume_preview_content.read()#简历预览页面的html
        soup=BeautifulSoup(resume_preview_message)
        self.image=soup.find("img").get('src')#照片
        basic_summary=str(soup.find("div","summary"))#抽取的html代码段
        items=basic_summary.split()
        index=0
        for item in items:
            elements= re.findall(ur"[\u4e00-\u9fa5]+",item.decode('utf8'))#匹配里面的汉字
            if elements:
                for element in elements:
                        index+=1
                        if index==2 :
                            self.sex = element#性别
                        if index==3 :
                            self.marriage = element#婚否
                        if index==7:
                            self.hukou= element#户口所在地
                        if index==8:
                            self.livingplace=element#现居地
                        if index==9:
                            self.profile=element#政治面貌
                        if index==10:
                            self.cerficationName=element#证件名称
    def SaveAsJson(self):
        dict={'name':self.name,'sex':self.sex,'birthday':self.birthday,'marriage':self.marriage,'hukou':self.hukou,'livingplace':self.livingplace,
              'profile':self.profile,'cerficationName':self.cerficationName,'cerficationNumber':self.cerficationNumber,
              'phone':self.phone,'emal':self.email,'image':self.image,'resume_preview_url':self.resume_preview_url}
        out_jscon = json.dumps(dict, ensure_ascii=False, encoding="utf-8").encode("utf-8")
        file_jscon = open('out_personal_json/' + self.name+  '.json', 'w')
        file_jscon.write(out_jscon)
        file_jscon.close()
if __name__ == '__main__':
    print "hello"
        
