from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get("https://www.baidu.com")
        element1 = self.driver.find_element_by_id("kw")
        element2 = self.driver.find_element_by_id("su")

        element1.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(element2)
        action.perform()

        action.scroll_from_element(element1,0,10000).perform()
        sleep(5)

if __name__ == '__main__':
    pytest.main()