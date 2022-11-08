# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：test_allure_case.py
# @IDE     ：PyCharm 
# @Date    ：2022/11/1 11:17
import allure
from .web_page import step_1, step_2, step_3


@allure.feature('编辑文章分类')
class TestDemoAllure:
    @allure.testcase('http://49.235.92.12:8080/zentao/testcase-view-6-2.html')
    @allure.story('输入文本，保存成功')
    @allure.title('编辑文章分类，输入中文，编辑成功')
    @allure.severity('blocker')
    def test_case1(self):
        """编辑文章分类，输入中文，编辑成功
        1、点文章分类导航标签
        2、编辑页面输入，分类名称
        3、点保存按钮"""
        step_1()
        step_2()
        step_3()

    @allure.testcase('http://49.235.92.12:8080/zentao/testcase-view-6-2.html')
    @allure.story('输入文本，保存成功')
    @allure.title('编辑文章分类，输入英文，编辑成功')
    def test_case2(self):
        """编辑文章分类，输入英文，编辑成功
        1、点文章分类导航标签
        2、编辑页面输入，分类名称
        3、点保存按钮"""
        step_1()
        step_2()
        step_3()

    @allure.issue('http://49.235.92.12:8080/zentao/testcase-view-6-2.html')
    @allure.story('输入为空，保存失败')
    @allure.title('编辑文章分类，输入为空，编辑失败')
    @allure.severity('critical')
    def test_case3(self):
        """编辑文章分类，不输入，编辑失败
        1、点文章分类导航标签
        2、编辑页面输入，分类名称
        3、点保存按钮"""
        step_1()
        step_2()
        step_3()
