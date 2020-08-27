from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_double_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com")
        element = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        darg_element = self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(darg_element,drop_element).perform()
        # action.click_and_hold(darg_element).release(drop_element).perform()
        action.click_and_hold(darg_element).move_to_element(drop_element).release().perform()
        sleep(5)

    def test_back(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element_input = self.driver.find_element_by_xpath('/html/body/label[1]/input').click()

        action = ActionChains(self.driver)
        action.send_keys("abcdef").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("lqm").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(5)


if __name__ == '__main__':
    pytest.main(['-v','-s','TestActionChains.py'])