# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：users_userinfo.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/31 13:56
# 个人信息页面
from common.base import Base


class UsersUserInfoPage(Base):
    nick_name = ('id','nick_name')
    save_btn = ('id','jsEditUserBtn')
    tips = ('class name','error-tips')
    dialog = ('css selector','#jsSuccessTips>.cont')

    def clear_nick_name(self):
        '''清除昵称'''
        self.clear(self.nick_name)

    def input_nick_name(self,text=''):
        '''输入昵称'''
        self.send(self.nick_name,text)

    def click_save_btn(self):
        '''点击保存按钮'''
        self.click(self.save_btn)

    def get_text1(self):
        '''获取昵称'''
        text = self.get_attribute(self.nick_name,'value')
        return text

    def get_tips(self):
        '''提示信息'''
        return self.get_text(self.tips)

    def get_dialog(self):
        '''获取保存成功的提示信息'''
        return self.get_text(self.dialog)