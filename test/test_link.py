import pytest,allure

@allure.link("http://www.baidu.com",name="百度")
def test_link():
    print("链接测试")

@allure.testcase("test_case_link","关联用例")
def test_testcase():
    print("test_testcase")

@allure.issue("bugid","问题")
def test_issue():
    print("test_issue")