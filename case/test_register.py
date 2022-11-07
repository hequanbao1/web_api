# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：test_register.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/24 17:33
from pages.register_page import RegisterPage


class TestRegister():

    def test_register_success(self,driver,base_url):
        '''注册成功案例'''
        register = RegisterPage(driver,base_url)
        register.open('/users/register/')
        # 操作步骤
        register.input_email('2012652@qq.com')
        register.input_password('123456')
        register.click_register_btn()
        actual_result = register.register_success_text()
        # 断言
        assert actual_result == '尊敬的用户，您好，账户已激活成功！'

    def test_register_email_existed(self, driver, base_url):
        '''注册成功案例'''
        register = RegisterPage(driver, base_url)
        register.open('/users/register/')
        # 操作步骤
        register.input_email('789456@qq.com')
        register.input_password('123456')
        register.click_register_btn()
        actual_result = register.register_success_text()
        # 断言
        assert actual_result != '尊敬的用户，您好，账号已激活成功！'





