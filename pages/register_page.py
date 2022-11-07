# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：register_page.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/24 17:17
from common.base import Base


class RegisterPage(Base):
    email_loc = ('id','id_email')
    email_div_loc = ('xpath','//*[@id="id_email"]/..')
    password_loc = ('id','id_password')
    password_div_loc = ('xpath', '//*[@id="id_password"]/..')
    btn_loc = ('id','jsEmailRegBtn')

    # 注册成功提示信息
    success_loc = ('css selector','body>h1')

    def input_email(self,text):
        '''输入邮箱'''
        self.send(self.email_loc,text)

    def input_password(self,text):
        '''输入密码'''
        self.send(self.password_loc,text)

    def click_register_btn(self):
        '''点击注册按钮'''
        self.click(self.btn_loc)

    def register_success_text(self):
        return self.get_text(self.success_loc)

    def get_email_class(self):
        '''获取邮箱输入框class属性'''
        return self.get_attribute(self.email_div_loc,'class')

    def get_password_class(self):
        '''获取邮箱输入框class属性'''
        return self.get_attribute(self.password_div_loc,'class')

    def get_eamil_attr(self,attr='value'):
        '''获取邮箱输入框的属性'''
        return self.get_attribute(self.email_loc,attr)

    def clear_eamil(self):
        '''清除邮箱输入框中的内容'''
        return self.clear(self.email_loc)

    def get_password_attr(self,attr='value'):
        '''获取密码输入框中的属性'''
        return self.get_attribute(self.password_loc,attr)

    def clear_password(self):
        '''清除密码输入框内容'''
        return self.clear(self.password_loc)

    def get_link_href(self,xpath_loc):
        '''获取超链接地址'''
        loc = ('xpath',xpath_loc)
        return self.get_attribute(loc,'href')




