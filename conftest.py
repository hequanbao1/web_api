# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：conftest.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/25 10:46
import pytest
from selenium import webdriver
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.feedbackiframe_page import FeedBackIframe
from pages.users_userinfo import UsersUserInfoPage


@pytest.fixture(scope='session',name='driver')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def base_url():
    url = 'http://49.235.92.12:8200'
    return url


@pytest.fixture(scope='session')
def registerPage(driver,base_url):
    register = RegisterPage(driver, base_url)
    return register


@pytest.fixture(scope='session')
def loginPage(driver,base_url):
    login = LoginPage(driver,base_url)
    return login


@pytest.fixture(scope='session')
def feedBackIframe(driver,base_url):
    feedback = FeedBackIframe(driver,base_url)
    return feedback


@pytest.fixture(scope='session')
def login_driver(driver,loginPage:LoginPage):
    '''登录'''
    loginPage.open("/users/login/")
    loginPage.input_username('1234@qq.com')
    loginPage.input_password('123456')
    loginPage.click_login()
    return driver


@pytest.fixture(scope='session')
def userinfo(login_driver,base_url):
    '''个人信息'''
    userinfo = UsersUserInfoPage(login_driver,base_url)
    return userinfo
