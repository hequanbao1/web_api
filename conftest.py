# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：conftest.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/25 10:46
import pytest
import platform
from selenium import webdriver
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.feedbackiframe_page import FeedBackIframe
from pages.users_userinfo import UsersUserInfoPage
from selenium.webdriver.chrome.options import Options


# 下面的方法可以判断当前系统是windows还是linux

@pytest.fixture(scope="session", name="driver")
def browser():
    """定义全局driver"""
    if platform.system() == 'windows':
        _driver = webdriver.Chrome()
        _driver.maximize_window()

    else:
        # linux启动
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速，如果软件渲染器没有就位
        chrome_options.add_argument('--headless')  # 无界面

        _driver = webdriver.Chrome(chrome_options=chrome_options)

        yield _driver
        _driver.quit()


# @pytest.fixture(scope='session',name='driver')
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


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
