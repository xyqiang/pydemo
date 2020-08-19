import pytest,allure,time
from selenium import webdriver

@allure.testcase("http://github.com",)
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data",["java","python","html"])
def test_search(test_data):
    with allure.step("打开浏览器"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")

    with allure.step("关键字搜索"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存截图"):
        driver.save_screenshot("./result/test.png")
        allure.attach.file("./result/test.png",attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()