# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：test_feedbackiframe.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/28 20:51
# 意见反馈页面测试用例
import pytest
from pages.feedbackiframe_page import FeedBackIframe


class TestFeedBack():

    @pytest.fixture(autouse=True)
    def open(self,feedBackIframe:FeedBackIframe):
        feedBackIframe.open('/users/feedbackiframe/')
        feedBackIframe.to_iframe()

    def test_all_type(self,feedBackIframe:FeedBackIframe):
        text = feedBackIframe.select_all()
        print(str(text))
        assert text == ['改进建议', '页面布局', '提BUG']

    def test_selected_type(self,feedBackIframe:FeedBackIframe):
        '''切换选项内容后检查切换的内容是否正确'''
        # 先切换到页面布局
        feedBackIframe.select_subject(value='页面布局')
        print(str('切换后的选项内容:{}'.format(feedBackIframe.selected_type())))
        assert feedBackIframe.selected_type() == '页面布局'
        # 切换到提bug
        feedBackIframe.select_subject(value='提BUG')
        print(str('切换后的选项内容:{}'.format(feedBackIframe.selected_type())))
        assert feedBackIframe.selected_type() == '提BUG'
        # 切换到改进建议
        feedBackIframe.select_subject(value='改进建议')
        print(str('切换后的选项内容:{}'.format(feedBackIframe.selected_type())))
        assert feedBackIframe.selected_type() == '改进建议'

    @pytest.mark.parametrize('test_input',['改进建议', '页面布局', '提BUG'])
    def test_selected_type1(self,feedBackIframe:FeedBackIframe,test_input):
        feedBackIframe.select_subject(value=test_input)
        print(str('切换后的选项内容:{}'.format(feedBackIframe.selected_type())))
        assert feedBackIframe.selected_type() == test_input

    def test_feedback_send(self,feedBackIframe:FeedBackIframe):
        # 反馈类型
        feedBackIframe.select_subject(value='页面布局')
        # 反馈内容
        feedBackIframe.input_feedback_text('测试反馈内容输入')
        # 联系方式
        feedBackIframe.input_email('123456@qq.com')
        # 点击send按钮
        feedBackIframe.click_send()
        # 获取到alter中的内容,并点击确定按钮
        alter_text = feedBackIframe.get_alert_text()
        assert alter_text == '提交成功！'

    @pytest.mark.parametrize('test_input,result',[
        [{'value':'页面布局','text':'测试反馈内容输入','email':'123456@qq.com'},"提交成功！"],
        [{'value':'改进建议','text':'测试反馈内容输入','email':'123456@qq.com'},"提交成功！"],
        [{'value': '提BUG', 'text': '测试反馈内容输入', 'email': '123456@qq.com'}, "提交成功！"],
        [{'value': '提BUG', 'text': '', 'email': '123456@qq.com'}, "提交成功！"],
        [{'value': '提BUG', 'text': '', 'email': ''}, "提交成功！"]
    ])
    def test_feedback_send1(self, feedBackIframe: FeedBackIframe,test_input,result):
        # 反馈类型
        feedBackIframe.select_subject(value=test_input['value'])
        # 反馈内容
        feedBackIframe.input_feedback_text(test_input['text'])
        # 联系方式
        feedBackIframe.input_email(test_input['email'])
        # 点击send按钮
        feedBackIframe.click_send()
        # 获取到alter中的内容,并点击确定按钮
        alter_text = feedBackIframe.get_alert_text()
        assert alter_text == result




