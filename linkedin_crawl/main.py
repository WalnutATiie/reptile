    # -*- coding: utf-8 -*-
'''
2015.03.3118:28
Kang Li
'''
from code_html_analysis.html_parser_linkedin import Person
from code_simulated_loading.login_linkedin import Linkedin
def main():
    f = Linkedin("", "")
    if f.login() == 1:
        client = f.get_client()
        res=client.get('http://www.linkedin.com/profile/preview?locale=zh_CN&trk=prof-0-sb-preview-primary-button')#profile预览界面
        person_information = Person(res.content)
        person_information.parse_basic()
        person_information.saveProfilePage()
        person_information.SaveAsJson()
        connections_url = person_information.get_connections_url()
        for single_url in connections_url:
            res = client.get(single_url)
            friend_information = Person(res.content)
            friend_information.parse_basic()
            friend_information.SaveAsJson()
            friend_information.saveProfilePage()
if __name__ == '__main__':
    main()
