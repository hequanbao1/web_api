# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：web_page.py
# @IDE     ：PyCharm 
# @Date    ：2022/11/1 11:14
import allure


@allure.step('步骤：点1按钮')
def step_1():
    print('步骤111111-------')


@allure.step('步骤：点2按钮')
def step_2():
    print('步骤22222-------')


@allure.step('步骤：点3按钮')
def step_3():
    print('步骤33333-------')