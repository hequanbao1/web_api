# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：login_page.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/28 12:43
from common.base import Base


class LoginPage(Base):
    username_loc = ('id','username')
    password_loc = ('id','password_l')
    login_btn = ('id','jsLoginBtn')
    login_error = ('id','jsLoginTips')

    def input_username(self,user=''):
        '''用户名输入框内容'''
        self.send(self.username_loc,user)

    def input_password(self,paw=''):
        '''用户名密码'''
        self.send(self.password_loc,paw)

    def click_login(self):
        '''登录按钮'''
        self.click(self.login_btn)

    def login_error_text(self):
        '''获取到登录失败时的提示语'''
        return self.get_text(self.login_error)



