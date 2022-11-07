# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：test_login.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/28 14:17
import pytest
from pages.login_page import LoginPage


class TestLoginPage():

    @pytest.fixture(autouse=True)
    def open_login(self,loginPage:LoginPage):
        loginPage.open('/users/login/')

    def test_login_success(self,loginPage:LoginPage,base_url):
        '''登陆页-用户名、密码正确登录成功'''
        loginPage.input_username('123456@qq.com')
        loginPage.input_password('123456')
        loginPage.click_login()
        result = loginPage.driver.current_url
        print('实际结果:',result)
        assert result == base_url + '/'

    def test_login_error(self,loginPage:LoginPage):
        '''用户名错误，密码正确点击登录'''
        loginPage.input_username('123456')
        loginPage.input_password('123456')
        loginPage.click_login()
        result = loginPage.login_error_text()
        print('登录失败结果展示：',result)
        assert result == '用户名或密码错误'


