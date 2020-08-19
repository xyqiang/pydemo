import pytest,allure

@allure.feature("测试登录模块")
class TestLogin():

    @allure.story("正常登录")
    def test_login(self):
        print("test_login")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("test_login_fail")

    @allure.story("登录步骤")
    def test_login_step(self):
        with allure.step("步骤"):
            print("test_login_step")



