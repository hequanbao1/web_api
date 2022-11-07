# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：feedbackiframe_page.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/28 17:47
# 意见反馈页面
from common.base import Base


class FeedBackIframe(Base):
    iframe = ('id','feedback_iframe')
    feedback_type = ('name','subject')
    feedback_text = ('id','mesaage')
    feedback_email = ('xpath','//*[@placeholder="email"]')
    send_btn = ('xpath','//input[@class="button"]')

    def to_iframe(self):
        '''切换到iframe中'''
        self.switch_iframe(self.iframe)

    def select_subject(self,value):
        '''选择对应的下拉选项'''
        self.select_by_value(self.feedback_type,value)


    def select_all(self):
        '''获取到下拉框的所有选项内容'''
        all_type = self.select_object(self.feedback_type).options
        all_text = [i.text for i in all_type]
        return all_text

    def selected_type(self):
        '''获取到当前选中的选项类型'''
        all_type = self.select_object(self.feedback_type).first_selected_option
        return all_type.text


    def input_feedback_text(self,text=''):
        '''输入反馈内容'''
        self.send(self.feedback_text,text)

    def input_email(self,text=''):
        '''输入邮箱'''
        self.send(self.feedback_email,text)

    def click_send(self):
        '''点击send提交按钮'''
        self.click(self.send_btn)


