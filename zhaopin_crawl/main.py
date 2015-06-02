    # -*- coding: utf-8 -*-
#2015.03.11 18:28
#Kang Li
from code_html_analysis.html_analysis_zhaopin import UserInfo
from code_simulated_loading.loading_zhaopin import Zhaopin
def main():
    f = Zhaopin("", "")#模拟登陆
    if f.login() == 1:
        opener=f.getopener()
        user_info = UserInfo(opener)#新建用户信息类
        user_info.getUserInfo()#信息抽取
        user_info.saveResumePage()
        user_info.SaveAsJson()#保存为json
if __name__ == '__main__':
    main()
    

