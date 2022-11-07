# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：test_userinfo.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/31 14:20
from pages.users_userinfo import UsersUserInfoPage
import pytest
import time


class TestUsersUserInfo():

    @pytest.fixture(autouse=True)
    def open(self,userinfo:UsersUserInfoPage):
        userinfo.open('/users/userinfo/')
        userinfo.clear_nick_name()

    def test_nick_name(self,userinfo:UsersUserInfoPage):
        userinfo.input_nick_name('')
        userinfo.click_save_btn()
        print(userinfo.get_tips())
        assert userinfo.get_tips() == '请输入昵称！'

    def test_get_dialog(self,userinfo:UsersUserInfoPage):
        userinfo.input_nick_name('测试dialog22')
        userinfo.click_save_btn()
        time.sleep(0.2)
        print(userinfo.get_dialog())
        print('当前昵称展示：', userinfo.get_text1())
        assert userinfo.get_dialog() == '个人信息修改成功！'

